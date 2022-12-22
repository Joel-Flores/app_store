all_tables = [
    "DROP TABLE IF EXISTS claim_team;",
    "DROP TABLE IF EXISTS work_orders;",
    "DROP TABLE IF EXISTS codes;",
    "DROP TABLE IF EXISTS team_retirement;",
    "DROP TABLE IF EXISTS cable_reel_assignment;",
    "DROP TABLE IF EXISTS material_assignment;",
    "DROP TABLE IF EXISTS equipment_assignment;",
    "DROP TABLE IF EXISTS cable_reel;",
    "DROP TABLE IF EXISTS materials;",
    "DROP TABLE IF EXISTS serial_equipments;",
    "DROP TABLE IF EXISTS user;",
    "DROP TABLE IF EXISTS staff;",
    "DROP TABLE IF EXISTS model_equipments;",
    "DROP TABLE IF EXISTS status_materials;",
    "DROP TABLE IF EXISTS positions;",
    "DROP TABLE IF EXISTS type_works;",
    
    """CREATE TABLE positions(
        id INT PRIMARY KEY AUTO_INCREMENT,
        position VARCHAR (15) NOT NULL
    );
    """,
    """CREATE TABLE status_materials(
	    id INT PRIMARY KEY AUTO_INCREMENT,
        status_material VARCHAR(25)
    );
    """,
    """CREATE TABLE model_equipments(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name_model VARCHAR(20) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
    );
    """,
    """CREATE TABLE type_works(
        id INT PRIMARY KEY AUTO_INCREMENT,
        type_work VARCHAR(10) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
    );
    """,
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
    );
    """,
    """CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(25) UNIQUE NOT NULL,
        password VARCHAR(110) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        staff_id INT NOT NULL,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (staff_id) REFERENCES staff(id)
        );
    """,
    """CREATE TABLE serial_equipments(
        id INT PRIMARY KEY AUTO_INCREMENT,
        cm_mac VARCHAR(30) NOT NULL,
        cm_mac_two VARCHAR(30) NOT NULL DEFAULT 0,
        card_number INT NOT NULL DEFAULT 0,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        model_id INT NOT NULL,
        status_id INT NOT NULL,
        created_by INT NOT NULL,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (model_id) REFERENCES model_equipments(id),
        FOREIGN KEY (status_id) REFERENCES status_materials(id),
        FOREIGN KEY (created_by) REFERENCES user(id)
    );
    """,
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
        status_id INT NOT NULL,
        created_by INT NOT NULL,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (status_id) REFERENCES status_materials(id),
        FOREIGN KEY (created_by) REFERENCES user(id)
    );
    """,
    """CREATE TABLE cable_reel(
		id INT PRIMARY KEY AUTO_INCREMENT,
        serials VARCHAR(30) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        status_id INT NOT NULL,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (status_id) REFERENCES status_materials(id)
	);
    """,
    """CREATE TABLE equipment_assignment(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        serial_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (user_id) REFERENCES user(id),
        FOREIGN KEY (serial_id) REFERENCES serial_equipments(id)
    );
    """,
    """CREATE TABLE material_assignment(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        material_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (user_id) REFERENCES user(id),
        FOREIGN KEY (material_id) REFERENCES materials(id)
    );
    """,
    """CREATE TABLE cable_reel_assignment(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        reel_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (user_id) REFERENCES user(id),
        FOREIGN KEY (reel_id) REFERENCES cable_reel(id)
    );
    """,
    """CREATE TABLE team_retirement(
        id INT PRIMARY KEY AUTO_INCREMENT,
        technical_id INT NOT NULL,
        serial_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (technical_id) REFERENCES user(id),
        FOREIGN KEY (serial_id) REFERENCES serial_equipments(id)
    );
    """,
    """CREATE TABLE codes(
        id INT PRIMARY KEY AUTO_INCREMENT,
        code BIGINT NOT NULL,
        technical_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (technical_id) REFERENCES user(id)
    );
    """,
    """CREATE TABLE work_orders(
		id INT PRIMARY KEY AUTO_INCREMENT,
        work_order BIGINT NOT NULL,
        serial_id INT NOT NULL,
        material_id INT NOT NULL,
        code_id INT NOT NULL,
        technical_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (serial_id) REFERENCES serial_equipments(id),
        FOREIGN KEY (material_id) REFERENCES materials(id),
        FOREIGN KEY (code_id) REFERENCES codes(id),
        FOREIGN KEY (technical_id) REFERENCES user(id)
    );
    """,
    """CREATE TABLE claim_team(
        id INT PRIMARY KEY AUTO_INCREMENT,
        code_id INT NOT NULL,
        work_order_id INT NOT NULL,
        serial_id INT NOT NULL,
        technical_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (code_id) REFERENCES codes(id),
        FOREIGN KEY (work_order_id) REFERENCES work_orders(id),
        FOREIGN KEY (serial_id) REFERENCES serial_equipments(id),
        FOREIGN KEY (technical_id) REFERENCES user(id)
    );
    """
]

values_tables = [
    """INSERT INTO positions (position) 
        VALUES('Tecnico'), ('Almacen'), ('Aux almacen');
    """,
    """INSERT INTO status_materials (status_material) 
        VALUES ('Almacen'), ('Tecnico'), ('Usuario'), ('Retiro'), ('Con cliente'), ('Almacen Tigo');
    """,
    """INSERT INTO model_equipments (name_model) 
        VALUES ('Sin modelo'), ('Arris'), ('Hitron'), ('Verimatrix');
    """,
    """INSERT INTO type_works (type_work) 
        VALUES ('IP-0'), ('IP-1'), ('IP-2'), ('IP-3'), ('IP-3+IA-0'), ('IP-3+IA-1'), ('IA-0'),
        ('IA-1'), ('IA-2'), ('IA-3'), ('IA-4'), ('RECLAMO'), ('RETIRO');
    """
]