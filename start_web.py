#!/usr/bin/env python

from flask import Flask, render_template, request, url_for, flash, redirect, abort
import sqlite3

name = 'Brad'

# Flask Stuff #
app = Flask(__name__)

app.config['SECRET_KEY'] = 'R5m+n7b)jqh*k#t@w!f$g%d^v(x9y8z'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_inv_equip(equip_id):
    conn = get_db_connection()
    inv_item = conn.execute('SELECT * FROM items WHERE id = ?', 
                        (equip_id,)).fetchone()
    conn.close()
    if inv_item is None:
        abort(404)
    return inv_item


@app.route('/inventory')
def inventorylist():
    conn = get_db_connection()
    items = conn.execute('''SELECT * FROM items''').fetchall()
    print(items)
    conn.close()
    return render_template('inventorylist.html', 
                            title='List of Items',
                            username = name,
                            items=items)


@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    item = get_inv_equip(id)

    if request.method == 'POST':
        equiptype = request.form['equiptype']
        model = request.form['model']
        sn = request.form['sn']
        cal = request.form['cal']
        status = request.form['status']
        description = request.form['description']
        
        if not equiptype:
            flash('Equipment Type is required!')
        elif not model:
            flash('Model name is required!')
        elif not sn:
            flash('Serial Number is required!')
        elif not cal:
            flash('Calibration Due Date is required!')
        elif not status:
            flash('Current status is required!')
        elif not description:
            flash('Equipment Description is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE items SET equipment_type = ?, model = ?, serial_number = ?, calibration_due_date = ?, status = ?, description = ?'
                         ' WHERE id = ?',
                         (equiptype, model, sn, cal, status, description, id))

            conn.commit()
            conn.close()
            return redirect(url_for('inventorylist'))

    return render_template('edit.html', item=item)


@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    item = get_inv_equip(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM items WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(item['model']))
    return redirect(url_for('inventorylist'))


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        equiptype = request.form['equiptype']
        model = request.form['model']
        sn = request.form['sn']
        cal = request.form['cal']
        status = request.form['status']
        description = request.form['description']
        
        if not equiptype:
            flash('Equipment Type is required!')
        elif not model:
            flash('Model name is required!')
        elif not sn:
            flash('Serial Number is required!')
        elif not cal:
            flash('Calibration Due Date is required!')
        elif not status:
            flash('Current status is required!')
        elif not description:
            flash('Equipment Description is required!')
        else:
            conn = get_db_connection()
            conn.execute('''INSERT INTO items (equipment_type, model, serial_number, calibration_due_date, status, description)
                            VALUES (?, ?, ?, ?, ?, ?)''', (equiptype, model, sn, cal, status, description))
            conn.commit()
            conn.close()
            return redirect(url_for('inventorylist'))

    return render_template('create.html')


@app.route('/')
def index():
    conn = get_db_connection()
    #items = conn.execute('''SELECT * FROM items''').fetchall()
    items = conn.execute('''SELECT * FROM items WHERE calibration_due_date <= date('now', '-30 days')''').fetchall()
    print(items)
    conn.close()
    return render_template('index.html',
                            title='Home',
                            username = name,
                            items=items)

@app.route('/overdue_cal/')
def overdue_cal():
    conn = get_db_connection()
    items = conn.execute('''SELECT * FROM items WHERE calibration_due_date <= date('now', '-30 days')''').fetchall()
    print(items)
    conn.close()
    return render_template('overdue_cal.html',
                            title='Overdue Calibration',
                            username = name,
                            items=items)


















if __name__ == '__main__':
    #list_items()
    app.run()




