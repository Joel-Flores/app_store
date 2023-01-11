all_tables = [
    """DROP TABLE IF EXISTS code_reclaim_equipments;""",
    """DROP TABLE IF EXISTS code_materials;""",
    """DROP TABLE IF EXISTS code_work_orders;""",
    """DROP TABLE IF EXISTS material_assignment;""",
    """DROP TABLE IF EXISTS material_store_and_tech;""",
    """DROP TABLE IF EXISTS materials;""",
    """DROP TABLE IF EXISTS reel_assignment;""",
    """DROP TABLE IF EXISTS cable_reel;""",
    """DROP TABLE IF EXISTS equipments_assignment;""",
    """DROP TABLE IF EXISTS equipments_serial;""",
    """DROP TABLE IF EXISTS codes;""",
    """DROP TABLE IF EXISTS user;""",
    """DROP TABLE IF EXISTS staff;""",
    """DROP TABLE IF EXISTS type_works;""",
    """DROP TABLE IF EXISTS equipments_model;""",
    """DROP TABLE IF EXISTS status_materials;""",
    """DROP TABLE IF EXISTS positions;""",

    """CREATE TABLE positions(
        id INT PRIMARY KEY AUTO_INCREMENT,
        position VARCHAR (15) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
    );""",
    """CREATE TABLE status_materials(
        id INT PRIMARY KEY AUTO_INCREMENT,
        status_material VARCHAR(100),
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
    );""",
    """CREATE TABLE equipments_model(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name_model VARCHAR(20) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
    );""",
    """CREATE TABLE type_works(
        id INT PRIMARY KEY AUTO_INCREMENT,
        type_work VARCHAR(10) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
    );""",
    """CREATE TABLE staff(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_name VARCHAR(15) NOT NULL,
        user_name_two VARCHAR(15) DEFAULT "None",
        user_lastname VARCHAR(15) NOT NULL,
        user_lastname_two VARCHAR(15) DEFAULT "None",
        positions_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (positions_id) REFERENCES positions(id)
    );""",
    """CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(25) UNIQUE NOT NULL,
        password VARCHAR(110) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        staff_id INT NOT NULL,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (staff_id) REFERENCES staff(id)
    );""",

    """CREATE TABLE codes(
        id INT PRIMARY KEY AUTO_INCREMENT,
        code BIGINT NOT NULL,
        technical_id INT NOT NULL,
        checkout BIT DEFAULT FALSE,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (technical_id) REFERENCES user(id)
    );""",
    """CREATE TABLE equipments_serial(
        id INT PRIMARY KEY AUTO_INCREMENT,
        cm_mac VARCHAR(30) NOT NULL,
        cm_mac_two VARCHAR(30) NOT NULL DEFAULT 0,
        card_number INT NOT NULL DEFAULT 0,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        model_id INT NOT NULL,
        registered_by INT NOT NULL,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (model_id) REFERENCES equipments_model(id),
        FOREIGN KEY (registered_by) REFERENCES user(id)
    );""",
    """CREATE TABLE equipments_assignment(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        serial_id INT NOT NULL,
        status_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        registered_by INT NOT NULL,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (user_id) REFERENCES user(id),
        FOREIGN KEY (serial_id) REFERENCES equipments_serial(id),
        FOREIGN KEY (status_id) REFERENCES status_materials(id),
        FOREIGN KEY (registered_by) REFERENCES user(id)
    );""",


    """CREATE TABLE cable_reel(
		id INT PRIMARY KEY AUTO_INCREMENT,
        serial VARCHAR(30) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        registered_by INT NOT NULL,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (registered_by) REFERENCES user(id)
	);""",
    """CREATE TABLE reel_assignment(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        reel_id INT NOT NULL,
        registered_by INT NOT NULL,
        status_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (user_id) REFERENCES user(id),
        FOREIGN KEY (reel_id) REFERENCES cable_reel(id),
        FOREIGN KEY (registered_by) REFERENCES user(id),
        FOREIGN KEY (status_id) REFERENCES status_materials(id)
    );""",

    """CREATE TABLE materials(
        id INT PRIMARY KEY AUTO_INCREMENT,
        cable_hdmi INT NOT NULL DEFAULT 0,
        cable_rca INT NOT NULL DEFAULT 0,
        spliter_two INT NOT NULL DEFAULT 0,
        spliter_three INT NOT NULL DEFAULT 0,
        remote_control INT NOT NULL DEFAULT 0,
        connector_int INT NOT NULL DEFAULT 0,
        connector_ext INT NOT NULL DEFAULT 0,
        power_supply INT NOT NULL DEFAULT 0,
        q_span INT NOT NULL DEFAULT 0,
        cp_black INT NOT NULL DEFAULT 0,
        sp_black INT NOT NULL DEFAULT 0,
        sp_withe INT NOT NULL DEFAULT 0,
        satellite_dish INT NOT NULL DEFAULT 0,
        lnb INT NOT NULL DEFAULT 0,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        registered_by INT NOT NULL,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (registered_by) REFERENCES user(id)
    );""",
    """CREATE TABLE material_store_and_tech(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        material_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (user_id) REFERENCES user(id),
        FOREIGN KEY (material_id) REFERENCES materials(id)
    );""",
    """CREATE TABLE material_assignment(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        material_id INT NOT NULL,
        registered_by INT NOT NULL,
        status_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (user_id) REFERENCES user(id),
        FOREIGN KEY (material_id) REFERENCES materials(id),
        FOREIGN KEY (registered_by) REFERENCES user(id),
        FOREIGN KEY (status_id) REFERENCES status_materials(id)
    );""",
    """CREATE TABLE code_work_orders(
		id INT PRIMARY KEY AUTO_INCREMENT,
        work_order BIGINT NOT NULL,
        type_work_id INT NOT NULL,
        serial_id INT NOT NULL,
        code_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (type_work_id) REFERENCES type_works(id),
        FOREIGN KEY (serial_id) REFERENCES equipments_serial(id),
        FOREIGN KEY (code_id) REFERENCES codes(id)
    );""",
    """CREATE TABLE code_materials(
		id INT PRIMARY KEY AUTO_INCREMENT,
        material_id INT NOT NULL,
        code_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (material_id) REFERENCES materials(id),
        FOREIGN KEY (code_id) REFERENCES codes(id)
    );""",
    """CREATE TABLE code_reclaim_equipments(
        id INT PRIMARY KEY AUTO_INCREMENT,
        code_id INT NOT NULL,
        work_order_id INT NOT NULL,
        serial_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (code_id) REFERENCES codes(id),
        FOREIGN KEY (work_order_id) REFERENCES code_work_orders(id),
        FOREIGN KEY (serial_id) REFERENCES equipments_serial(id)
    );"""
]

values_tables = [
    """INSERT INTO positions (position) 
    VALUES('admin'), ('almacen'), ('tecnico');""",

    """INSERT INTO equipments_model (name_model) 
    VALUES ('Sin modelo'), ('arris'), ('hitron'), ('verimatrix');""",

    """INSERT INTO status_materials (status_material) 
    VALUES ('ingreso a almacen desde tigo'), ('devuelto a el almacen tigo'), 
    ('asignado al tecnico'), ('ingreso a almacen desde el tecnico'), 
    ('con cliente'), ('asignado a un codigo'), ('retirado de un codigo'), ('entregado a almacen'), 
    ('facturado al usuario'), ('facturado al tecnico');""",

    """INSERT INTO type_works (type_work) 
    VALUES ('IP-0'), ('IP-1'), ('IP-2'), ('IP-3'), ('IP-3+IA-0'), ('IP-3+IA-1'), ('IA-0'),
    ('IA-1'), ('IA-2'), ('IA-3'), ('IA-4'), ('RECLAMO'), ('RETIRO');""",

    """INSERT INTO staff (user_name, user_lastname, positions_id) 
    VALUES ('data red', 'administrador', 1), ('samuel', 'almacen', 2), ('alvaro', 'tecnico', 3), ('gonzalo', 'tecnico', 3);""",

    """INSERT INTO user (username, password, staff_id) 
    VALUES
    ('admin','pbkdf2:sha256:260000$PML0wrXjURAIg7aE$d85807b931172f014b087c097694d4466789da7a9bbc34d531a989948d13a9ce',1),
    ('almacen','pbkdf2:sha256:260000$PML0wrXjURAIg7aE$d85807b931172f014b087c097694d4466789da7a9bbc34d531a989948d13a9ce',2),
    ('tec_1','pbkdf2:sha256:260000$PML0wrXjURAIg7aE$d85807b931172f014b087c097694d4466789da7a9bbc34d531a989948d13a9ce',3),
    ('tec_2','pbkdf2:sha256:260000$PML0wrXjURAIg7aE$d85807b931172f014b087c097694d4466789da7a9bbc34d531a989948d13a9ce',4);""",

    """INSERT INTO materials(registered_by)
    VALUES (1), (1), (1);""",

    """INSERT INTO material_store_and_tech(user_id, material_id)
    VALUES(1, 1), (2, 1), (3, 2), (4, 3);""",

    """INSERT INTO equipments_serial (cm_mac, model_id, registered_by) 
    VALUES 
    ('Sin equipo', 1, 2);"""
]