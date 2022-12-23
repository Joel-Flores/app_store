def update_reel_store(db, c, reels_id, user_id):
    query = 'INSERT INTO cable_reel_assignment (user_id, reel_id) VALUES (%s, %s);'
    for reel_id in reels_id:
        values = [user_id, reel_id['id']]
        c.execute(query, values)
        db.commit()