import json
import os

class ConfigManager:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """Loads configuration from a JSON file."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        else:
            # Return a default configuration if the file doesn't exist
            return {
                "database": {
                    "host": "localhost",
                    "port": 5432,
                    "user": "admin"
                },
                "api_key": "default_key_123"
            }

    def get(self, key, default=None):
        """Retrieves a configuration value."""
        return self.config.get(key, default)

    def set(self, key, value):
        """Sets a configuration value and saves it to the file."""
        self.config[key] = value
        self.save_config()

    def save_config(self):
        """Saves the current configuration to the JSON file."""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

    def display_config(self):
        """Prints the current configuration."""
        print("\nCurrent Configuration:")
        print(json.dumps(self.config, indent=4))

if __name__ == "__main__":
    # Initialize ConfigManager. It will create config.json if it doesn't exist.
    # This demonstrates loading initial state or default values.
    cm = ConfigManager()
    cm.display_config()

    # Demonstrate getting a configuration value
    db_host = cm.get("database", {}).get("host")
    print(f"\nDatabase Host: {db_host}")

    # Demonstrate setting and saving a configuration value
    # This simulates updating a setting in a running system.
    new_api_key = "super_secret_key_456"
    print(f"\nUpdating API Key to: {new_api_key}")
    cm.set("api_key", new_api_key)

    # Display the updated configuration
    cm.display_config()

    # Demonstrate getting the updated value
    updated_api_key = cm.get("api_key")
    print(f"\nUpdated API Key retrieved: {updated_api_key}")

    # Clean up the created config file (optional)
    # import os
    # if os.path.exists('config.json'):
    #     os.remove('config.json')
    #     print("\nCleaned up config.json")
