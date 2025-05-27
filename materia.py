"""
Materia source code

Coded by: ViCoder32

17-04-2025
"""
from flask import Flask, request, jsonify, render_template
from sqlite3 import connect
from random import randint
import socket

app = Flask(__name__)

def get_local_ipv4() -> str:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except socket.error: return "127.0.0.1"

def modify_query(text: str, filter_dict: dict) -> str:
    """
    Algoritm which adds attributes from client in SQL query
    """
    return f"{text}\n{''.join([f'{i} BETWEEN {j[0]} AND {j[1]}, ' for i, j in filter_dict.items()])}"[:-2]

@app.get("/")
def index_page():
    """
    Function returns general page of Materia, and while didn`t nothing more
    """
    return render_template("index.html")

@app.get("/about")
def about_page():
    """
    Function returns page which contains desctiption of this projects
    """
    return render_template("about.html")

@app.get("/getapi")
def getapi():
    """
    Function returns page offer of buy accept to Materia API
    """
    return render_template("getapi.html")

@app.get("/api/count")
def material_count():
    """
    API function which returns count of strings in database
    """
    with connect("proto_material.db") as db:
        return str(db.cursor().execute("SELECT seq FROM sqlite_sequence WHERE name='material'").fetchall()[0][0])

@app.get("/api/material_desc_list")
def material_desc_list():
    """
    API function returns short values about materials in pseudo-random range which length equal 5.
    Also support update of feed, but unique of values depends to size of database.
    The more - the better
    """
    num = randint(6, 50)
    with connect("proto_material.db") as db:
        return jsonify([{"name": i[0], "desc": i[1], "photo": i[2]} for i in db.cursor().execute(f"SELECT name, desc, photo FROM material WHERE id BETWEEN {num - 5} AND {num}").fetchall()])

@app.get("/api/material_detail_choose&<name>")
def material_detail_choose(name):
    """
    API function which returns detail data about material by name.
    Exists to do increase productivity
    """
    with connect("proto_material.db") as db:
        query = db.cursor().execute(modify_query("""
    SELECT
    thermal_cap,
    thermal_exp,
    thermal_dur,
    electro_con,
    dielectric_const,
    piezo_prop,
    super_con,
    magnet_const,
    coercive,
    res_magnet,
    refractive_index,
    photo_elastic,
    tensile_str,
    fluid,
    hardness,
    jung_module,
    plastic,
    fragility,
    impact_str,
    deform_speed,
    relax_ten,
    corrosion_res,
    fire_res,
    chemical_iner,
    solubility,
    molding_prop,
    cutting,
    malleability,
    hardenability,
    wear_res,
    fatigue_str,
    radiation_res,
    tightness,
    phase_structure,
    seed_size,
    porosity
    FROM material WHERE
    """, request.get_json())).fetchall()
        return jsonify({
    "thermal_cap": query[4],
    "thermal_exp": query[6],
    "dielectric_const": query[9],
    "piezo_prop": query[10],
    "super_con": query[11],
    "magnet_const": query[12],
    "coercive": query[13],
    "res_magnet": query[14],
    "refractive_index": query[16],
    "lumin": query[17],
    "photo_elastic": query[18],
    "tensile_str": query[19],
    "fluid": query[20],
    "hardness": query[21],
    "jung_module": query[22],
    "plastic": query[23],
    "fragility": query[24],
    "impact_str": query[25],
    "deform_speed": query[26],
    "relax_ten": query[27],
    "corrosion_res": query[28],
    "fire_res": query[29],
    "chemical_iner": query[30],
    "solubility": query[31],
    "molding_prop": query[32],
    "cutting": query[33],
    "malleability": query[34],
    "hardenability": query[35],
    "wear_res": query[36],
    "fatigue_str": query[37],
    "radiation_res": query[38],
    "tightness": query[39],
    "phase_structure": query[41],
    "seed_size": query[42],
    "porosity": query[43]
})
@app.post("/api/material_choose&<mode>")
def material_choose(request, mode):
    """
    API function which returns data about material by attributes
    and has two modes
    0: Returns all attributes of material
    1: Returns only general attributes
    """
    match int(mode):
        case 0:
            with connect("proto_material.db") as db:
                query = db.cursor().execute(modify_query("""
SELECT
name,
desc,
photo,
thermal_con,
thermal_cap,
melting,
thermal_exp,
electro_con,
dielectric_const,
piezo_prop,
super_con,
magnet_const,
coercive,
res_magnet,
transparent,
refractive_index,
lumin,
photo_elastic,
tensile_str,
fluid,
hardness,
jung_module,
plastic,
fragility,
impact_str,
deform_speed,
relax_ten,
corrosion_res,
fire_res,
chemical_iner,
solubility,
molding_prop,
cutting,
malleability,
hardenability,
wear_res,
fatigue_str,
radiation_res,
tightness,
crystal_structure,
phase_structure,
seed_size,
porosity
FROM material WHERE
""", request.get_json())).fetchall()
            return jsonify({
"name": query[0],
"desc": query[1],
"photo": query[2],
"thermal_con": query[3],
"thermal_cap": query[4],
"melting": query[5],
"thermal_exp": query[6],
"thermal_dur": query[7],
"electro_con": query[8],
"dielectric_const": query[9],
"piezo_prop": query[10],
"super_con": query[11],
"magnet_const": query[12],
"coercive": query[13],
"res_magnet": query[14],
"transparent": query[15],
"refractive_index": query[16],
"lumin": query[17],
"photo_elastic": query[18],
"tensile_str": query[19],
"fluid": query[20],
"hardness": query[21],
"jung_module": query[22],
"plastic": query[23],
"fragility": query[24],
"impact_str": query[25],
"deform_speed": query[26],
"relax_ten": query[27],
"corrosion_res": query[28],
"fire_res": query[29],
"chemical_iner": query[30],
"solubility": query[31],
"molding_prop": query[32],
"cutting": query[33],
"malleability": query[34],
"hardenability": query[35],
"wear_res": query[36],
"fatigue_str": query[37],
"radiation_res": query[38],
"tightness": query[39],
"crystal_structure": query[40],
"phase_structure": query[41],
"seed_size": query[42],
"porosity": query[43]
})
        case 1:
            with connect("proto_material.db") as db:
                query = db.cursor().execute(modify_query("""
        SELECT
        name,
        desc,
        photo,
        thermal_con,
        melting,
        thermal_dur,
        electro_con,
        transparent,
        lumin,
        crystal_structure
        FROM material WHERE
        """, request.get_json())).fetchall()
                return jsonify({
        "name": query[0],
        "desc": query[1],
        "photo": query[2],
        "thermal_con": query[3],
        "melting": query[5],
        "thermal_dur": query[7],
        "electro_con": query[8],
        "transparent": query[15],
        "lumin": query[17],
        "crystal_structure": query[40]
    })

def main() -> None:
    """
    Entry point of API, nothing intresting
    """
    app.run(host=get_local_ipv4(), port=80)

if __name__ == '__main__': main()