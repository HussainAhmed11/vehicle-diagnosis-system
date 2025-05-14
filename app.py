from flask import Flask, request, render_template, jsonify
from experta import Fact
from rules import CarExpert, MotorcycleExpert, BoatExpert
from car import Car, Motorcycle, Boat

app = Flask(__name__)

SYMPTOMS = {
    "car": [
        "Car won't start",
        "Black smoke from exhaust",
        "Clicking noise when turning key",
        "Engine overheating",
        "Car vibration while driving",
        "Fuel smell inside car",
        "Increased fuel consumption",
        "Engine abnormal noise",
        "Oil/water leakage",
        "Squealing noise when braking",
        "Steering feels heavy",
        "Dashboard warning lights on",
        "Car pulls to one side",
        "Strange smell from AC",
        "Transmission slipping"
    ],
    "motorcycle": [
        "Motorcycle won't start",
        "Excessive exhaust smoke",
        "Engine overheating",
        "Chain noise",
        "Difficulty shifting gears",
        "Oil leakage",
        "Brake squeal",
        "Handlebar vibration",
        "Headlight not working",
        "Engine stalling"
    ],
    "boat": [
        "Boat engine won't start",
        "Excessive smoke from engine",
        "Engine overheating",
        "Propeller vibration",
        "Water leakage in hull",
        "Steering hard to turn",
        "Battery not charging",
        "Fuel smell in cabin",
        "Loss of engine power",
        "Warning lights on dashboard"
    ]
}

def normalize_symptom(symptom):
    return symptom.strip().lower()

@app.route('/', methods=['GET', 'POST'])
def diagnose():
    result = None
    user_symptom = ""
    vehicle_type = "car"
    symptoms = SYMPTOMS[vehicle_type]

    if request.method == 'POST':
        vehicle_type = request.form.get('vehicle_type', 'car')
        symptoms = SYMPTOMS.get(vehicle_type, [])
        user_symptom = request.form['symptom']
        normalized_symptom = normalize_symptom(user_symptom)
        matched = False

        for s in symptoms:
            if normalize_symptom(s) == normalized_symptom:
                user_symptom = s
                matched = True
                break

        if not matched:
            # إذا لم يتم التطابق مع أي عرض، نرسل عرض فارغ ليعمل القاعدة الافتراضية
            user_symptom = ""

        if vehicle_type == "car":
            engine = CarExpert()
            fact_class = Car
        elif vehicle_type == "motorcycle":
            engine = MotorcycleExpert()
            fact_class = Motorcycle
        else:
            engine = BoatExpert()
            fact_class = Boat

        engine.reset()
        engine.declare(Fact(action='diagnose'))
        engine.declare(fact_class(symptom=user_symptom))

        # طباعة لتتبع القيم المرسلة (للتأكد من صحة البيانات)
        print(f"DEBUG: Vehicle={vehicle_type}, Symptom='{user_symptom}'")

        engine.run()

        for fact in engine.facts.values():
            if isinstance(fact, Fact) and 'result' in fact:
                result = fact['result']
                break

    return render_template(
        'diagnose.html',
        result=result,
        symptoms=symptoms,
        user_symptom=user_symptom,
        vehicle_type=vehicle_type
    )

@app.route('/get_symptoms/<vehicle_type>')
def get_symptoms(vehicle_type):
    return jsonify(SYMPTOMS.get(vehicle_type, []))

if __name__ == '__main__':
    app.run(debug=True)
    