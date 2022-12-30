#registrar entradas de materiales y equipos
# -ingreso de equipos y salida del id
    *INSERT INTO equipments_serial(cm_mac,cm_mac_two,card_number, model_id, registered_by) VALUES(%s, %s, %s, %s, %s);
    *SELECT id FROM equipments_serial WHERE registered_by = %s ORDER BY id DESC LIMIT 1;
# -ingreso del material y salida del id
    *INSERT INTO materials (cable_hdmi, cable_rca, spliter_two, spliter_three, remote_control, connector_int, connector_ext, power_supply, q_span, cp_black, sp_black, sp_withe, satellite_dish, lnb, registered_by) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s %s, %s, %s, %s, %s);
    *SELECT id FROM materials WHERE registered_by = %s ORDER BY id DESC LIMIT 1;
#- ingreso de carretas y salida del id
    *INSERT INTO cable_reel(serial, registered_by) VALUES(%s, %s);
    *SELECT id FROM cable_reel WHERE registered_by = %s ORDER BY id DESC LIMIT 1;

# -suma o resta del material del tecnico o del almacen
    *UPDATE material_store_and_tech SET cable_hdmi = %s, cable_rca = %s, spliter_two = %s, spliter_three = %s, remote_control = %s, connector_int = %s, connector_ext = %s, power_supply = %s, q_span, cp_black = %s, sp_black = %s, sp_withe = %s, satellite_dish = %s, lnb = %s WHERE id = %s;



# ingreso a almacen desde tigo
    # -ingreso de equipos y salida del id
    *INSERT INTO equipments_store(user_id, serial_id, status_id) VALUES(%s, %s, 1);
    # -ingreso del material y salida del id
    *INSERT INTO material_store_assignment(user_id, material_id, status_id) VALUES(%s, %s, 1);
    # -sumamos el material al almacen
    #- ingreso de carretas y salida del id
    *INSERT INTO cable_reel_store(user_id, reel_id, status_id) VALUES(%s, %s, 1);



#devuelto a el almacen tigo
    # -buscamos el ultimo registro del equipo activo, y actualizamos el sistema de almacen, el sistema de equipos activos en el almacen
    SELECT id FROM equipments_serial WHERE cm_mac = %s AND register_active = True;
    *UPDATE equipments_store SET register_active = False WHERE serial_id = %s;
    *UPDATE equipments_serial SET register_active = False WHERE id = %s;
    *INSERT INTO equipments_store(user_id, serial_id, status_id) VALUES(%s, %s, 2);
    # -ingreso del material y salida del id
    *INSERT INTO material_store_assignment(user_id, material_id, status_id) VALUES(%s, %s, 2);
    # -restamos el material al almacen



#asignado al tecnico
    # buscamos el ultimo registro del equipo activo, y actualizamos el sistema de almacen y asignamos al sistema del tecnico
    SELECT id FROM equipments_serial WHERE cm_mac = %s AND register_active = True;
    *UPDATE equipments_store SET register_active = False WHERE serial_id = %s;
    *INSERT INTO equipments_store(user_id, serial_id, status_id) VALUES(%s, %s, 3);
    INSERT INTO equipments_tech(user_id, serial_id, status_id) VALUES(%s, %s, 3);
    # -ingreso del material y salida del id
    INSERT INTO material_tech_assignment(user_id, material_id, registered_by, status_id) VALUES(%s, %s, %s, 3);
    # -sumamos el material al tecnico
    # -asignamos las carretas al tecnico
    SELECT id FROM cable_reel WHERE serial = %s AND register_active = True;
    *UPDATE cable_reel_store SET register_active = False WHERE reel_id = %s;
    INSERT INTO cable_reel_store(user_id, reel_id, status_id) VALUES(%s, %s, 3);
    INSERT INTO cable_reel_tech(user_id, reel_id, registered_by, status_id) VALUES(%s, %s, %s, 3);


#ingreso a almacen desde el tecnico
    # -buscamos los equipos registrados por el tecnico que esten activos, actuañizamos los equipos del tecnico y del almacen
    SELECT id, cm_mac FROM equipments_serial WHERE registered_by = %s AND register_active = True;
    UPDATE equipments_tech SET register_active = False WHERE serial_id = %s;
    *INSERT INTO equipments_store(user_id, serial_id, status_id) VALUES(%s, %s, 4);
    INSERT INTO equipments_tech(user_id, serial_id, status_id) VALUES (%s, %s, 8);
    # -ingreso del material y salida del id
    *INSERT INTO material_store_assignment(user_id, material_id, status_id) VALUES(%s, %s, 4);
    # -sumamos el material al almacen
    INSERT INTO material_tech_assignment(user_id, material_id, status_id) VALUES(%s, %s, 8);
    # -restamos el material al tecnico
    SELECT id FROM cable_reel WHERE serial = %s AND register_active = True;
    UPDATE cable_reel_tech SET register_active = False WHERE reel_id = %;
    INSERT INTO cable_reel_tech(user_id, reel_id, registered_by, status_id) VALUES(%s, %s, %s, 8);
    *UPDATE cable_reel_store SET register_active = False WHERE reel_id = %;
    INSERT INTO cable_reel_store(user_id, reel_id, status_id) VALUES(%s, %s, 4);
    UPDATE cable_reel SET register_active = False WHERE id = %s;

#con cliente
      # -buscamos los equipos registrados en el sistema de alamcen que enten devueltos por el tecnico
      SELECT id FROM equipments_serial WHERE cm_mac = %s AND register_active = True;
      *UPDATE equipments_store SET register_active = False WHERE serial_id = %s;
      *INSERT INTO equipments_store(user_id, serial_id, status_id) VALUES(%s, %s, 5);

#facturado al usuario
      # -buscamos los equipos registrados en el sistema de alamcen que enten devueltos por el tecnico
      SELECT id FROM equipments_serial WHERE cm_mac = %s AND register_active = True;
      *UPDATE equipments_store SET register_active = False WHERE serial_id = %s;
      # -buscamos el codigo de donde se retiro el equipo
      SELECT code_id FROM code_work_orders WHERE serial_id = %s;
      INSERT INTO equipments_invoiced(user_id, serial_id, code_id, status_id) VALUES(%s, %s, %s, 9);
      *UPDATE equipments_serial SET register_active = False WHERE id = %s;

#facturado al tecnico
      # -buscamos los equipos registrados en el sistema de alamcen que enten devueltos por el tecnico
      SELECT id FROM equipments_serial WHERE cm_mac = %s AND register_active = True;
      *UPDATE equipments_store SET register_active = False WHERE serial_id = %s;
      # -buscamos el codigo de donde se retiro el equipo
      SELECT code_id FROM code_work_orders WHERE serial_id = %s;
      INSERT INTO equipments_invoiced(user_id, serial_id, code_id, status_id) VALUES(%s, %s, %s, 10);
      *UPDATE equipments_serial SET register_active = False WHERE id = %s;
      