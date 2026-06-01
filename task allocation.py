import os
import shutil

def organize_jpg_files(source_dir, target_dir):
    """
    Moves all .jpg files from source_dir to target_dir.
    You will need to create a 'source' folder and put some test .jpg files in it to test this.
    """
    # Ensure source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: The source directory '{source_dir}' does not exist.")
        return
        
    # Create target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created target directory '{target_dir}'.")

    moved_count = 0
    
    # Iterate through files in the source directory
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_dir, filename)
            target_path = os.path.join(target_dir, filename)
            
            # Move the file
            shutil.move(source_path, target_path)
            print(f"Moved: {filename}")
            moved_count += 1
            
    print(f"\nAutomation complete. Successfully moved {moved_count} .jpg file(s).")

if __name__ == "__main__":
    # Change these paths to match folders on your computer
    source_folder = "./unorganized_images"
    target_folder = "./jpg_collection"
    organize_jpg_files(source_folder, target_folder)