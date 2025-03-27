import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty inputs
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with values or "N/A" if missing
        personalized_invitation = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A") or "N/A"
            personalized_invitation = personalized_invitation.replace(f"{{{key}}}", value)

        # Generate output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, "w") as output_file:
                output_file.write(personalized_invitation)
        except Exception as e:
            print(f"Error writing to file {output_filename}: {e}")
