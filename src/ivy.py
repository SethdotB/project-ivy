carbon_forecast = { 
    "prediction_1" : { 
        "time" : "Now",
        "carbon_intensity" : 420
    },
    "prediction_2" : { 
        "time" : "+1 hour",
        "carbon_intensity" : 390
    },
    "prediction_3" : { 
        "time" : "+2 hours",
        "carbon_intensity" : 310
    },
    "prediction_4" : { 
        "time" : "+3 hours",
        "carbon_intensity" : 245
    },
    "prediction_5" : { 
        "time" : "+4 hours",
        "carbon_intensity" : 270
    },
    "prediction_6" : { 
        "time" : "+5 hours",
        "carbon_intensity" : 350
    }         
}

def find_cleanest_window(carbon_forecast):
    """
    Analyze carbon intensity forecasts to find the cleanest
    time to run a workload and calculate the potential reduction.
    """
    lowest_carbon_intensity = carbon_forecast["prediction_1"]["carbon_intensity"]
    cleanest_time = carbon_forecast["prediction_1"]["time"]

    # Compare each forecast to find the lowest carbon intensity.
    for prediction in carbon_forecast.values():
        if prediction["carbon_intensity"] < lowest_carbon_intensity:
            lowest_carbon_intensity = prediction["carbon_intensity"]
            cleanest_time = prediction["time"]

    current_carbon_intensity = carbon_forecast["prediction_1"]["carbon_intensity"]

    # Calculate the potential reduction compared to the current intensity.
    if current_carbon_intensity != 0:
        reduction_percentage = ((current_carbon_intensity - lowest_carbon_intensity) / current_carbon_intensity) * 100
    else:
        reduction_percentage = 0

    return cleanest_time, lowest_carbon_intensity, reduction_percentage

if __name__ == "__main__":
    cleanest_time, lowest_carbon_intensity, reduction_percentage = find_cleanest_window(carbon_forecast)

    print(f"Cleaner window detected: {cleanest_time} with a carbon intensity of {lowest_carbon_intensity}.")
    print(f"Potential carbon intensity reduction: {reduction_percentage:.2f}%")