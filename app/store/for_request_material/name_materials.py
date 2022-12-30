
def name_materials(c):
    c.execute('SHOW COLUMNS FROM materials;')
    name_materials = list()
    for data in c.fetchall():
        if data['Field'] != 'id' and data['Field'] != 'status_id' and data['Field'] != 'created_in' and data['Field'] != 'created_by' and data['Field'] != 'register_active':
            name_materials.append(data['Field'])
    return name_materials