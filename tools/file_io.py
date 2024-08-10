from datetime import datetime
import os

def save_markdown(task_output, filename_prefix="TravelPlan_", date_format="%Y-%m-%d", encoding="utf-8"):
  """
  Saves the provided content to a Markdown file with a timestamped filename within the "Travel Doc" folder.

  Args:
      task_output (object): The data to be saved as Markdown.
      filename_prefix (str, optional): Prefix for the filename. Defaults to "TravelPlan_".
      date_format (str, optional): Format string for the date in the filename. Defaults to "%Y-%m-%d" (YYYY-MM-DD).
      encoding (str, optional): Encoding for the file. Defaults to "utf-8".

  Returns:
      str: The filename of the saved Markdown file.
  """

  try:
    # Get current date
    today_date = datetime.now().strftime(date_format)

    # Create filename with timestamp
    filename_md = f"{filename_prefix}{today_date}.md"

    # Create "Travel Doc" folder if it doesn't exist
    travel_doc_folder = "Travel Doc"
    if not os.path.exists(travel_doc_folder):
      os.makedirs(travel_doc_folder)

    # Create full path to the file
    full_path = os.path.join(travel_doc_folder, filename_md)

    # Process content
    result = task_output.result if hasattr(task_output, 'result') else task_output
    if callable(result):
      result = result()
    if not isinstance(result, str):
      result = str(result)

    # Save content to file
    with open(full_path, 'w', encoding=encoding) as file:
      file.write(result)

    print(f"Markdown file saved as: {full_path}")
    return full_path  # Return the filename for potential further processing

  except Exception as e:
    print(f"Error saving Markdown file: {e}")
    return None  # Return None on error (optional)
