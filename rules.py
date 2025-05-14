from experta import KnowledgeEngine, Rule, Fact
from car import Car, Motorcycle, Boat

class CarExpert(KnowledgeEngine):
    @Rule(Fact(action='diagnose'), Car(symptom="Car won't start"))
    def battery_issue(self):
        self.declare(Fact(result="Car: Possible dead battery, starter motor, or ignition switch issue."))

    @Rule(Fact(action='diagnose'), Car(symptom="Black smoke from exhaust"))
    def black_smoke(self):
        self.declare(Fact(result="Car: Excess fuel, faulty injectors, or clogged air filter."))

    @Rule(Fact(action='diagnose'), Car(symptom="Clicking noise when turning key"))
    def clicking_noise(self):
        self.declare(Fact(result="Car: Weak battery or starter motor issue."))

    @Rule(Fact(action='diagnose'), Car(symptom="Engine overheating"))
    def engine_overheating(self):
        self.declare(Fact(result="Car: Possible coolant leak, faulty thermostat, or radiator issue."))

    @Rule(Fact(action='diagnose'), Car(symptom="Car vibration while driving"))
    def vibration(self):
        self.declare(Fact(result="Car: Unbalanced tires, worn suspension, or engine mount issue."))

    @Rule(Fact(action='diagnose'), Car(symptom="Fuel smell inside car"))
    def fuel_smell(self):
        self.declare(Fact(result="Car: Fuel leak or faulty fuel injector."))

    @Rule(Fact(action='diagnose'), Car(symptom="Increased fuel consumption"))
    def increased_fuel(self):
        self.declare(Fact(result="Car: Dirty air filter, faulty oxygen sensor, or tire pressure issue."))

    @Rule(Fact(action='diagnose'), Car(symptom="Engine abnormal noise"))
    def abnormal_noise(self):
        self.declare(Fact(result="Car: Engine wear, low oil, or loose components."))

    @Rule(Fact(action='diagnose'), Car(symptom="Oil/water leakage"))
    def leakage(self):
        self.declare(Fact(result="Car: Damaged gasket, hose, or seal."))

    @Rule(Fact(action='diagnose'), Car(symptom="Squealing noise when braking"))
    def squealing_brake(self):
        self.declare(Fact(result="Car: Worn brake pads or dirty rotors."))

    @Rule(Fact(action='diagnose'), Car(symptom="Steering feels heavy"))
    def heavy_steering(self):
        self.declare(Fact(result="Car: Low power steering fluid or steering system issue."))

    @Rule(Fact(action='diagnose'), Car(symptom="Dashboard warning lights on"))
    def dashboard_warning(self):
        self.declare(Fact(result="Car: Check the car manual for warning light meanings. There may be an electrical or sensor issue."))

    @Rule(Fact(action='diagnose'), Car(symptom="Car pulls to one side"))
    def pulls_one_side(self):
        self.declare(Fact(result="Car: Wheel alignment or brake issue."))

    @Rule(Fact(action='diagnose'), Car(symptom="Strange smell from AC"))
    def ac_smell(self):
        self.declare(Fact(result="Car: Mold in AC system or cabin air filter needs replacement."))

    @Rule(Fact(action='diagnose'), Car(symptom="Transmission slipping"))
    def transmission_slip(self):
        self.declare(Fact(result="Car: Low transmission fluid or worn transmission components."))

    @Rule(Fact(action='diagnose'), Car())
    def default(self):
        self.declare(Fact(result="Car: No diagnosis found for this symptom. Please provide more details or consult a professional mechanic."))


class MotorcycleExpert(KnowledgeEngine):
    @Rule(Fact(action='diagnose'), Motorcycle(symptom="Motorcycle won't start"))
    def battery_issue(self):
        self.declare(Fact(result="Motorcycle: Possible dead battery, faulty spark plug, or fuel system issue."))

    @Rule(Fact(action='diagnose'), Motorcycle(symptom="Excessive exhaust smoke"))
    def smoke(self):
        self.declare(Fact(result="Motorcycle: Oil burning or fuel mixture issue."))

    @Rule(Fact(action='diagnose'), Motorcycle(symptom="Engine overheating"))
    def overheating(self):
        self.declare(Fact(result="Motorcycle: Low coolant, blocked radiator, or oil issue."))

    @Rule(Fact(action='diagnose'), Motorcycle(symptom="Chain noise"))
    def chain_noise(self):
        self.declare(Fact(result="Motorcycle: Check chain tension and lubrication."))

    @Rule(Fact(action='diagnose'), Motorcycle(symptom="Difficulty shifting gears"))
    def shifting(self):
        self.declare(Fact(result="Motorcycle: Clutch cable or gearbox issue."))

    @Rule(Fact(action='diagnose'), Motorcycle(symptom="Oil leakage"))
    def oil_leak(self):
        self.declare(Fact(result="Motorcycle: Check gaskets and seals."))

    @Rule(Fact(action='diagnose'), Motorcycle(symptom="Brake squeal"))
    def brake_squeal(self):
        self.declare(Fact(result="Motorcycle: Worn brake pads or dirty rotors."))

    @Rule(Fact(action='diagnose'), Motorcycle(symptom="Handlebar vibration"))
    def handlebar_vibration(self):
        self.declare(Fact(result="Motorcycle: Unbalanced wheels or loose parts."))

    @Rule(Fact(action='diagnose'), Motorcycle(symptom="Headlight not working"))
    def headlight(self):
        self.declare(Fact(result="Motorcycle: Burnt bulb or wiring issue."))

    @Rule(Fact(action='diagnose'), Motorcycle(symptom="Engine stalling"))
    def stalling(self):
        self.declare(Fact(result="Motorcycle: Idle adjustment or fuel delivery issue."))

    @Rule(Fact(action='diagnose'), Motorcycle())
    def default(self):
        self.declare(Fact(result="Motorcycle: No diagnosis found for this symptom. Please provide more details or consult a professional mechanic."))


class BoatExpert(KnowledgeEngine):
    @Rule(Fact(action='diagnose'), Boat(symptom="Boat engine won't start"))
    def engine_start(self):
        self.declare(Fact(result="Boat: Dead battery, fuel issue, or starter motor problem."))

    @Rule(Fact(action='diagnose'), Boat(symptom="Excessive smoke from engine"))
    def smoke(self):
        self.declare(Fact(result="Boat: Oil burning, fuel mixture, or engine wear."))

    @Rule(Fact(action='diagnose'), Boat(symptom="Engine overheating"))
    def overheating(self):
        self.declare(Fact(result="Boat: Blocked water intake, low coolant, or impeller issue."))

    @Rule(Fact(action='diagnose'), Boat(symptom="Propeller vibration"))
    def propeller_vibration(self):
        self.declare(Fact(result="Boat: Damaged or unbalanced propeller."))

    @Rule(Fact(action='diagnose'), Boat(symptom="Water leakage in hull"))
    def hull_leak(self):
        self.declare(Fact(result="Boat: Hull crack or loose fittings."))

    @Rule(Fact(action='diagnose'), Boat(symptom="Steering hard to turn"))
    def steering(self):
        self.declare(Fact(result="Boat: Steering cable or hydraulic issue."))

    @Rule(Fact(action='diagnose'), Boat(symptom="Battery not charging"))
    def battery(self):
        self.declare(Fact(result="Boat: Faulty alternator or wiring."))

    @Rule(Fact(action='diagnose'), Boat(symptom="Fuel smell in cabin"))
    def fuel_smell(self):
        self.declare(Fact(result="Boat: Fuel leak or venting issue."))

    @Rule(Fact(action='diagnose'), Boat(symptom="Loss of engine power"))
    def power_loss(self):
        self.declare(Fact(result="Boat: Fouled propeller, dirty fuel filter, or engine wear."))

    @Rule(Fact(action='diagnose'), Boat(symptom="Warning lights on dashboard"))
    def warning_lights(self):
        self.declare(Fact(result="Boat: Check manual for warning light meaning."))

    @Rule(Fact(action='diagnose'), Boat())
    def default(self):
        self.declare(Fact(result="Boat: No diagnosis found for this symptom. Please provide more details or consult a professional mechanic."))
