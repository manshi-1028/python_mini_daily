
from datetime import datetime

from services.nutritionix import get_exercise_data
from services.sheety import save_workout


def main():
    print("=" * 50)
    print("        EXERCISE TRACKER")
    print("=" * 50)

    exercise_input = input(
        "\nTell me which exercise you did today: "
    ).strip()

    if not exercise_input:
        print("Please enter an exercise.")
        return

    try:
        exercises = get_exercise_data(exercise_input)

        if not exercises:
            print("No exercise was detected.")
            return

        now = datetime.now()

        for exercise in exercises:
            workout = {
                "date": now.strftime("%d/%m/%Y"),
                "time": now.strftime("%H:%M:%S"),
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }

            save_workout(workout)

            print("\nWorkout saved successfully!")
            print("-" * 40)
            print(f"Exercise : {workout['exercise']}")
            print(f"Duration : {workout['duration']} minutes")
            print(f"Calories : {workout['calories']} kcal")
            print("-" * 40)

    except Exception as error:
        print(f"\nSomething went wrong: {error}")


if __name__ == "__main__":
    main()
