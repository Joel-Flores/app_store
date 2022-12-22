def tech_name(id, technicals):
    for technical in technicals:
        if technical['id'] == id:
            name_technical = technical
    return name_technical