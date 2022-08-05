import json

bmi_data = [
    {
        "value":[0,18.4],
        "bmi_category":"under weight",
        "health_risk":"malnutrition risk",
    },
    {
        "value":[18.5,24.9],
        "bmi_category":"normal weight",
        "health_risk":"low risk",
    },
     {
        "value":[25,29.9],
        "bmi_category":"over weight",
        "health_risk":"enhanced risk",
    },
     {
        "value":[30,34.9],
        "bmi_category":"moderately obese",
        "health_risk":"medium risk",
    },
     {
        "value":[35,39.9],
        "bmi_category":"severely obese",
        "health_risk":"high risk",
    },
     {
        "value":[40,999],
        "bmi_category":"very severely obese",
        "health_risk":"very high risk",
    },


]

def set_bmi_data_and_overweight(person,count):
    for bmi_category in bmi_data:
        person_bmi_value = person['bmi_value']
        if (person_bmi_value  >= bmi_category['value'][0] and 
               person_bmi_value <= bmi_category['value'][1]):
            person['bmi_category'] = bmi_category['bmi_category']
            person['health_risk'] = bmi_category['health_risk']
            if bmi_category['bmi_category'] =="over weight":
                count=count+1
    return count


    
with open('./input.json') as f:
    input_data = json.load(f)
    print("Given Input Data")
    print(input_data)
    total_over_weight = 0
    for person in input_data:
        height_in_meters = person['HeightCm']/100
        person['bmi_value'] = person['WeightKg']/(height_in_meters*height_in_meters)
        total_over_weight=set_bmi_data_and_overweight(person,count = total_over_weight)
    print("Total_no_of_OverWeight :",total_over_weight)
    output_data = json.dumps(input_data, indent=2)
    print("Resultant Data")
    print(output_data)
