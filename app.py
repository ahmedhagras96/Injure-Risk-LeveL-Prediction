from flask import Flask, render_template, request
import joblib

# __name__ is equal to app.py
app = Flask(__name__)

# load model from model.pck
model = joblib.load('model.pkl')



@app.route("/")
def home():
    return render_template('index.html')



@app.route("/predict", methods=["POST"])
def predict():
	Division =  request.form['Division']
	Observation_related_to =  request.form['Observation.related.to']
	Type_of_Activity =  request.form['Type.of.Activity']
	Observation_Category =  request.form['Observation.Category']
	Day =  request.form['Day']
	Month =  request.form['Month']
	Working_Condition =  request.form['Working.Condition']
	Machine_Condition =  request.form['Machine.Condition']
	Safety_Standards =  request.form['Safety.Standards']
	SOP_Combined =  request.form['SOP.Combined']
	Primary_Cause =  request.form['Primary.Cause']

Division_Bearing_Division=Division_Corporate_Services=Division_Engineering_Project=Division_Orissa_Projects=Division_Others=Division_Raw_Materials=
Division_Shared_Services=Division_Steel_Manufacturing=Observation_related_to_Employee=Type_of_Activity_Breaking_Sizing=Type_of_Activity_Construction=
Type_of_Activity_Errection_Commissioning=Type_of_Activity_Loading_Unloading=Type_of_Activity_Loco_Operation=Type_of_Activity_Maintenance=
Type_of_Activity_Operations=Type_of_Activity_Others=Type_of_Activity_Packing_of_finished_product=Type_of_Activity_Transportation=
Observation_Category_Caught_Between=Observation_Category_Confine_Space=Observation_Category_Electrical_Safety=Observation_Category_Environment=
Observation_Category_Excavation=Observation_Category_Eyes_Face=Observation_Category_Falling=Observation_Category_Fire_Safety=
Observation_Category_Gas_Safety=Observation_Category_Handrail=Observation_Category_Health=Observation_Category_Material_Handling
=Observation_Category_Mines_Safety=Observation_Category_Not_Followed=Observation_Category_Not_Maintained=Observation_Category_Not_Understood=
Observation_Category_Orderliness=Observation_Category_Others=Observation_Category_PPE=Observation_Category_Process_Safety=Observation_Category_Road_Safety=
Observation_Category_Temp_Elect_Wiring=Observation_Category_Tools_Equipment=Observation_Category_Uneasiness=Observation_Category_Workplace_Safety=
Day_Mon=Day_Sat=Day_Sun=Day_Thu=Day_Tue=Day_Wed=Month_August=Month_December=Month_February=Month_January=Month_July=Month_June=Month_March=Month_May=
Month_November=Month_October=Month_September=Working_Condition_Not_Applicable=Working_Condition_Single_Working=Machine_Condition_M_C_Working=
Machine_Condition_Not_Applicable=Safety_Standards_Confine_Space=Safety_Standards_Electrical_Safety=Safety_Standards_Excavation=
Safety_Standards_Fire_Safety=Safety_Standards_Gas_Cutting_Welding=Safety_Standards_Material_Handling=Safety_Standards_Mines_Safety=
Safety_Standards_Orderliness=Safety_Standards_Others=Safety_Standards_Others_Process_Safety=Safety_Standards_PPE=Safety_Standards_Process_Safety=
Safety_Standards_Road_Safety=Safety_Standards_Tools_Equipment=Safety_Standards_Workplace_Safety=SOP_Combined_SANF=SOP_Combined_SIF=
SOP_Combined_SINF=SOP_Combined_SNNR=SOP_Combined_SNR=Primary_Cause_Dashing_Collision=Primary_Cause_Derailment=Primary_Cause_Electrical_Flash=
Primary_Cause_Energy_Isolation=Primary_Cause_Equipment_Machinery_Damage=Primary_Cause_Fire_Explosion=Primary_Cause_Gas_Leakage=Primary_Cause_Hot_Metals=
Primary_Cause_Hydraulic_Pneumatic=Primary_Cause_Lifting_Tools_Tackles=Primary_Cause_Material_Handling=Primary_Cause_Medical_Ailment=
Primary_Cause_Occupational_Illness=Primary_Cause_Process_Incidents=Primary_Cause_Rail=Primary_Cause_Road_Incident=Primary_Cause_Run_Over=
Primary_Cause_Skidding=Primary_Cause_Slip_Trip_Fall=Primary_Cause_Structural_Integrity=Primary_Cause_Toxic_Chemicals=Primary_Cause_Workplace_Safety = 0



	if Division == 'Bearing Division':
		Division_Bearing_Division = 1
	elif Division == 'Corporate Services':
		Division_Corporate_Services = 1
	elif Division == 'Engineering & Project':
		Division_Engineering_Project = 1
    elif Division == 'Orissa Projects':
		Division_Orissa_Projects = 1
	elif Division == 'Others':
		Division_Others = 1
	elif Division == 'Raw Materials':
		Division_Raw_Materials = 1
	elif Division == 'Shared Services':
		Division_Shared_Services = 1
	elif Division == 'Steel Manufacturing':
		Division_Steel_Manufacturing = 1

	if Observation_related_to == 'Employee':
		Observation_related_to_Employee = 1
	
	if Type_of_Activity == 'Breaking & Sizing':
		Type_of_Activity_Breaking_Sizing = 1
	elif Type_of_Activity == 'Construction':
		Type_of_Activity_Construction = 1
	elif Type_of_Activity == 'Errection & Commissioning':
		Type_of_Activity_Errection_Commissioning = 1
    elif Type_of_Activity == 'Loading & Unloading':
		Type_of_Activity_Loading_Unloading = 1
	elif Type_of_Activity == 'Loco Operation':
		Type_of_Activity_Loco_Operation = 1
	elif Type_of_Activity == 'Maintenance':
		Type_of_Activity_Maintenance = 1
	elif Type_of_Activity == 'Operations':
		Type_of_Activity_Operations = 1
	elif Division == 'Others':
		Type_of_Activity_Others = 1
	elif Division == 'Packing of finished product':
		Type_of_Activity_Packing_of_finished_product = 1
	elif Division == 'Transportation':
		Type_of_Activity_Transportation = 1

	if Observation_Category == 'Caught Between':
		Observation_Category_Caught_Between = 1
	elif Observation_Category == 'Confine Space':
		Observation_Category_Confine_Space = 1
	elif Observation_Category == 'Electrical Safety':
		Observation_Category_Electrical_Safety = 1
    elif Observation_Category == 'Environment':
		Observation_Category_Environment = 1
	elif Observation_Category == 'Excavation':
		Observation_Category_Excavation = 1
	elif Observation_Category == 'Eyes & Face':
		Observation_Category_Eyes_Face = 1
	elif Observation_Category == 'Falling':
		Observation_Category_Falling = 1
	elif Observation_Category == 'Fire Safety':
		Observation_Category_Fire_Safety = 1
	elif Observation_Category == 'Gas Safety':
		Observation_Category_Gas_Safety = 1
	elif Observation_Category == 'Handrail':
		Observation_Category_Handrail = 1
	elif Observation_Category == 'Health':
		Observation_Category_Health = 1
	elif Observation_Category == 'Material Handling':
		Observation_Category_Material_Handling = 1
	elif Observation_Category == 'Mines Safety':
		Observation_Category_Mines_Safety = 1
	elif Observation_Category == 'Not Followed':
		Observation_Category_Not_Followed = 1
	elif Observation_Category == 'Not Maintained':
		Observation_Category_Not_Maintained = 1
	elif Observation_Category == 'Not Understood':
		Observation_Category_Not_Understood = 1
	elif Observation_Category == 'Orderliness':
		Observation_Category_Orderliness = 1
	elif Observation_Category == 'Others':
		Observation_Category_Others = 1
	elif Observation_Category == 'PPE':
		Observation_Category_PPE = 1
	elif Observation_Category == 'Process Safety':
		Observation_Category_Process_Safety = 1
	elif Observation_Category == 'Road Safety':
		Observation_Category_Road_Safety = 1
	elif Observation_Category == 'Temp. Elect. Wiring':
		Observation_Category_Temp_Elect_Wiring = 1
	elif Observation_Category == 'Tools & Equipment':
		Observation_Category_Tools_Equipment = 1
	elif Observation_Category == 'Uneasiness':
		Observation_Category_Uneasiness = 1
	elif Observation_Category == 'Workplace Safety':
		Observation_Category_Workplace_Safety = 1

	if Day == 'Mon':
		Day_Mon = 1
	elif Day == 'Sat':
		Day_Sat = 1
	elif Day == 'Sun':
		Day_Sun = 1
    elif Day == 'Thu':
		Day_Thu = 1
	elif Day == 'Tue':
		Day_Tue = 1
	elif Day == 'Wed':
		Day_Wed = 1

	if Month == 'August':
		Month_August = 1
	elif Month == 'December':
		Month_December = 1
	elif Month == 'February':
		Month_February = 1
    elif Month == 'January':
		Month_January = 1
	elif Month == 'July':
		Month_July = 1
	elif Month == 'June':
		Month_June = 1
    elif Month == 'March':
		Month_March = 1
	elif Month == 'May':
		Month_May = 1
	elif Month == 'November':
		Month_November = 1
    elif Month == 'October':
		Month_October = 1
	elif Month == 'September':
		Month_September = 1

	if Working_Condition == 'Not Applicable':
		Working_Condition_Not_Applicable = 1
	elif Working_Condition == 'Single Working':
		Working_Condition_Single_Working = 1

    
	if Machine_Condition == 'M/C Working':
		Machine_Condition_M_C_Working = 1
	elif Machine_Condition == 'Not Applicable':
		Machine_Condition_Not_Applicable = 1

	if Safety_Standards == 'Confine Space':
		Safety_Standards_Confine_Space = 1
	elif Safety_Standards == 'Electrical Safety':
		Safety_Standards_Electrical_Safety = 1
	elif Safety_Standards == 'Excavation':
		Safety_Standards_Excavation = 1
    elif Safety_Standards == 'Fire Safety':
		Safety_Standards_Fire_Safety = 1
	elif Safety_Standards == 'Gas Cutting & Welding':
		Safety_Standards_Gas_Cutting_Welding = 1
	elif Safety_Standards == 'Material Handling':
		Safety_Standards_Material_Handling = 1
    elif Safety_Standards == 'Mines Safety':
		Safety_Standards_Mines_Safety = 1
	elif Safety_Standards == 'Orderliness':
		Safety_Standards_Orderliness = 1
	elif Safety_Standards == 'Others':
		Safety_Standards_Others = 1
    elif Safety_Standards == 'Others,Process Safety':
		Safety_Standards_Others_Process_Safety = 1
	elif Safety_Standards == 'PPE':
		Safety_Standards_PPE = 1
	elif Safety_Standards == 'Process Safety':
		Safety_Standards_Process_Safety = 1
	elif Safety_Standards == 'Road Safety':
		Safety_Standards_Road_Safety = 1
    elif Safety_Standards == 'Tools & Equipment':
		Safety_Standards_Tools_Equipment = 1
	elif Safety_Standards == 'Workplace Safety':
		Safety_Standards_Workplace_Safety = 1

	if SOP_Combined == 'SANF':
		SOP_Combined_SANF = 1
	elif SOP_Combined == 'SIF':
		SOP_Combined_SIF = 1
	elif SOP_Combined == 'SINF':
		SOP_Combined_SINF = 1
    elif SOP_Combined == 'SNNR':
		SOP_Combined_SNNR = 1
	elif SOP_Combined == 'SNR':
		SOP_Combined_SNR = 1


	if Primary_Cause == 'Dashing/Collision':
		Primary_Cause_Dashing_Collision = 1
	elif Primary_Cause == 'Derailment':
		Primary_Cause_Derailment = 1
	elif Primary_Cause == 'Electrical Flash':
		Primary_Cause_Electrical_Flash = 1
    elif Primary_Cause == 'Energy Isolation':
		Primary_Cause_Energy_Isolation = 1
	elif Primary_Cause == 'Equipment Machinery Damage':
		Primary_Cause_Equipment_Machinery_Damage = 1
	elif Primary_Cause == 'Fire/Explosion':
		Primary_Cause_Fire_Explosion = 1
    elif Primary_Cause == 'Gas Leakage':
		Primary_Cause_Gas_Leakage = 1
	elif Primary_Cause == 'Hot Metals':
		Primary_Cause_Hot_Metals = 1
	elif Primary_Cause == 'Hydraulic/Pneumatic':
		Primary_Cause_Hydraulic_Pneumatic = 1
    elif Primary_Cause == 'Lifting Tools Tackles':
		Primary_Cause_Lifting_Tools_Tackles = 1
	elif Primary_Cause == 'Material Handling':
		Primary_Cause_Material_Handling = 1
	elif Primary_Cause == 'Medical Ailment':
		Primary_Cause_Medical_Ailment = 1
	elif Primary_Cause == 'Occupational Illness':
		Primary_Cause_Occupational_Illness = 1
    elif Primary_Cause == 'Process Incidents':
		Primary_Cause_Process_Incidents = 1
	elif Primary_Cause == 'Rail':
		Primary_Cause_Rail = 1
	elif Primary_Cause == 'Road Incident':
		Primary_Cause_Road_Incident = 1
    elif Primary_Cause == 'Run Over':
		Primary_Cause_Run_Over = 1
	elif Primary_Cause == 'Skidding':
		Primary_Cause_Skidding = 1
	elif Primary_Cause == 'Slip/Trip/Fall':
		Primary_Cause_Slip_Trip_Fall = 1
	elif Primary_Cause == 'Structural Integrity':
		Primary_Cause_Structural_Integrity = 1
    elif Primary_Cause == 'Toxic Chemicals':
		Primary_Cause_Toxic_Chemicals = 1
	elif Primary_Cause == 'Workplace Safety':
		Primary_Cause_Workplace_Safety = 1

	bike_count = model.predict([[Division_Bearing_Division,Division_Corporate_Services,Division_Engineering_Project,Division_Orissa_Projects,Division_Others,Division_Raw_Materials,
	Division_Shared_Services,Division_Steel_Manufacturing,Observation_related_to_Employee,Type_of_Activity_Breaking_Sizing,Type_of_Activity_Construction,
	Type_of_Activity_Errection_Commissioning,Type_of_Activity_Loading_Unloading,Type_of_Activity_Loco_Operation,Type_of_Activity_Maintenance,
	Type_of_Activity_Operations,Type_of_Activity_Others,Type_of_Activity_Packing_of_finished_product,Type_of_Activity_Transportation,
	Observation_Category_Caught_Between,Observation_Category_Confine_Space,Observation_Category_Electrical_Safety,Observation_Category_Environment,
	Observation_Category_Excavation,Observation_Category_Eyes_Face,Observation_Category_Falling,Observation_Category_Fire_Safety,
	Observation_Category_Gas_Safety,Observation_Category_Handrail,Observation_Category_Health,Observation_Category_Material_Handling
	,Observation_Category_Mines_Safety,Observation_Category_Not_Followed,Observation_Category_Not_Maintained,Observation_Category_Not_Understood,
	Observation_Category_Orderliness,Observation_Category_Others,Observation_Category_PPE,Observation_Category_Process_Safety,Observation_Category_Road_Safety,
	Observation_Category_Temp_Elect_Wiring,Observation_Category_Tools_Equipment,Observation_Category_Uneasiness,Observation_Category_Workplace_Safety,
	Day_Mon,Day_Sat,Day_Sun,Day_Thu,Day_Tue,Day_Wed,Month_August,Month_December,Month_February,Month_January,Month_July,Month_June,Month_March,Month_May,
	Month_November,Month_October,Month_September,Working_Condition_Not_Applicable,Working_Condition_Single_Working,Machine_Condition_M_C_Working,
	Machine_Condition_Not_Applicable,Safety_Standards_Confine_Space,Safety_Standards_Electrical_Safety,Safety_Standards_Excavation,
	Safety_Standards_Fire_Safety,Safety_Standards_Gas_Cutting_Welding,Safety_Standards_Material_Handling,Safety_Standards_Mines_Safety,
	Safety_Standards_Orderliness,Safety_Standards_Others,Safety_Standards_Others,Process_Safety,Safety_Standards_PPE,Safety_Standards_Process_Safety,
	Safety_Standards_Road_Safety,Safety_Standards_Tools___Equipment,Safety_Standards_Workplace_Safety,SOP_Combined_SANF,SOP_Combined_SIF,
	SOP_Combined_SINF,SOP_Combined_SNNR,SOP_Combined_SNR,Primary_Cause_Dashing_Collision,Primary_Cause_Derailment,Primary_Cause_Electrical_Flash,
	Primary_Cause_Energy_Isolation,Primary_Cause_Equipment_Machinery_Damage,Primary_Cause_Fire_Explosion,Primary_Cause_Gas_Leakage,Primary_Cause_Hot_Metals,
	Primary_Cause_Hydraulic_Pneumatic,Primary_Cause_Lifting_Tools_Tackles,Primary_Cause_Material_Handling,Primary_Cause_Medical_Ailment,
	Primary_Cause_Occupational_Illness,Primary_Cause_Process_Incidents,Primary_Cause_Rail,Primary_Cause_Road_Incident,Primary_Cause_Run_Over,
	Primary_Cause_Skidding,Primary_Cause_Slip_Trip_Fall,Primary_Cause_Structural_Integrity,Primary_Cause_Toxic_Chemicals,Primary_Cause_Workplace_Safety]])[0]
	return render_template("index.html", bike_count=bike_count)	




if __name__ == "__main__":
    app.run()
