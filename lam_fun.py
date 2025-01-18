 import json

def lambda_handler(event, context):
    """
    AWS Lambda function to add two numbers.
    Args:
        event (dict): Input event containing the numbers to add.
        context: Lambda Context runtime methods and attributes.

    Returns:
        dict: Response containing the result of the addition.
    """
    try:
        # Extract numbers from the event
        num1 = event.get('num1')
        num2 = event.get('num2')

        if num1 is None or num2 is None:
            raise ValueError("Both 'num1' and 'num2' must be provided in the input event.")

        # Ensure the numbers are integers or floats
        num1 = float(num1)
        num2 = float(num2)

        # Perform addition
        result = num1 + num2

        # Return the result
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Addition successful!",
                "num1": num1,
                "num2": num2,
                "result": result
            })
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": str(e),
                "message": "Failed to process the input."
            })
        }
