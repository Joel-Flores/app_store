from flask import flash
def update_tech_reel(db, c, reel_id, tech_id):
    for id in reel_id:
        #registrando que las carretas pasaron al tecnico
        query = 'UPDATE cable_reel SET status_id = %s WHERE id = %s;'
        values = [2, id]
        c.execute(query, values)
        db.commit()
        
        #registrando al tecnico la serie de la carreta
        query = 'INSERT INTO cable_reel_assignment(user_id, reel_id) VALUES (%s, %s);'
        values = [tech_id, id]
        c.execute(query, values)
        db.commit()
        flash('carreta asignada al tecnico')