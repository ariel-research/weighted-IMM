import fairpyx
import logging

# Each student's valuations sum to 1000 and each value is between 0 and 1000
instance = fairpyx.Instance(
    valuations={
        # Ranking: c1 (300) > c2 (200) > c4 (150) = c5 (150) > c3 (100) = c6 (100)
        "alon": {
            "c1": 300,
            "c2": 200,
            "c4": 150,
            "c5": 150,
            "c3": 100,
            "c6": 100
        },

        # Ranking: c3 (300) > c2 (200) > c4 (150) = c6 (150) > c1 (100) = c5 (100)
        "ruti": {
            "c3": 300,
            "c2": 200,
            "c4": 150,
            "c6": 150,
            "c1": 100,
            "c5": 100
        },

        # Ranking: c3 (250) > c1 (200) = c4 (200) > c2 (150) > c5 (100) = c6 (100)
        "sigalit": {
            "c3": 250,
            "c1": 200,
            "c4": 200,
            "c2": 150,
            "c5": 100,
            "c6": 100
        },

        # Ranking: c4 (300) > c3 (200) > c1 (150) = c5 (150) > c2 (100) = c6 (100)
        "uri": {
            "c4": 300,
            "c3": 200,
            "c1": 150,
            "c5": 150,
            "c2": 100,
            "c6": 100
        },

        # Ranking: c1 (250) > c4 (200) = c5 (200) > c3 (150) > c2 (100) = c6 (100)
        "ron": {
            "c1": 250,
            "c4": 200,
            "c5": 200,
            "c3": 150,
            "c2": 100,
            "c6": 100
        },
    },

    agent_capacities={
        "alon": 10,     # needs 10 credit points
        "ruti": 8,      # needs 8 credit points
        "sigalit": 16,  # needs 16 credit points
        "uri": 6,       # needs 6 credit points
        "ron": 4        # needs 4 credit points
    },

    item_capacities={
        "c1": 2,  # 2 seats
        "c2": 3,  # 3 seats
        "c3": 1,  # 2 seats
        "c4": 2,  # 2 seats
        "c5": 4,  # 4 seats
        "c6": 2   # 2 seats
    },

    item_weights={
        "c1": 2,  # 2 credit points
        "c2": 3,  # 3 credit points
        "c3": 4,  # 4 credit points
        "c4": 2,  # 2 credit points
        "c5": 3,  # 3 credit points
        "c6": 4   # 4 credit points
    }
)

# Explanation logger
string_explanation_logger = fairpyx.explanations.StringsExplanationLogger(
    agents=[name for name in instance.agents], language='he', level=logging.INFO)

# Divide using iterated maximum matching algorithm with the data above
map_agent_name_to_bundle = fairpyx.divide(
    algorithm=fairpyx.algorithms.iterated_maximum_matching_adjusted, 
    instance=instance,
    explanation_logger = string_explanation_logger)

# Print the result:
print("Result: \n",map_agent_name_to_bundle)

# Print the explanations:
example_student = "sigalit"
print(f"\nExample explanation: explanation sent to {example_student}:\n")
print(string_explanation_logger.map_agent_to_explanation()[example_student])





