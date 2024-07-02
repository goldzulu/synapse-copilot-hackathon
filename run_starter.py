# A Starter Kit version of the run.py file that can be used to run the API LLM for the Trello and TMDB scenarios.
from helper import *
import os
import sys

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

logger = logging.getLogger()

def main():
    # Load the configuration file
    config = yaml.load(open("config_starter.yaml", "r"), Loader=yaml.FullLoader)
    
    # check to see if the configuration file is being used
    if config is None:
        logger.error("Could not load configuration file")
        sys.exit(1)
    else:
        logger.info("Configuration file exist and loaded successfully")
    
    if config["use_config_file"] is True:
        # iterate through the config file and set the environment variables
        for key, value in config.items():
            os.environ[key.upper()] = str(value)
        logger.info("Environment variables set successfully to config values")
    else:
        load_dotenv()
        logger.info("Environment variables set successfully to .env values")
    logger.info("Make sure the keys are correctly set in the respective files!")
        

    logging.basicConfig(
        format="%(message)s",
        handlers=[logging.StreamHandler(ColorPrint())],
    )
    logger.setLevel(logging.INFO)

    # Select a scenario
    scenario = input(
        "Please select a scenario (airtable/elevenlabs/dalle3/zerocodekit/resend) Default (airtable): "
    )
    if (scenario == ""):
        scenario = "airtable"

    scenario = scenario.lower()
    api_spec, headers = None, None

    if scenario == "tmdb":
        #os.environ["TMDB_ACCESS_TOKEN"] = config["tmdb_access_token"]
        
        # Get the API Spec and Authorization headers
        api_spec, headers = process_spec_file(
            file_path="specs/tmdb_oas.json", token=os.environ["TMDB_ACCESS_TOKEN"]
        )
        # Example queries that will be used by default
        query_example = "Give me the number of movies directed by Sofia Coppola"

    elif scenario == "trello":
            
        replace_api_credentials_in_json(
            ###to replace all the key and token variables in the specs file with real values
            scenario=scenario,
            actual_key=os.environ["TRELLO_API_KEY"],
            actual_token=os.environ["TRELLO_TOKEN"]
        )
        api_spec, headers = process_spec_file(  ### to make the specs file minfy or smaller for for better processing
            file_path="specs/trello_oas.json",
            token=os.environ["TRELLO_TOKEN"],
            key=os.environ["TRELLO_API_KEY"]
        )

        # Replace the key and token placeholders in api_selector/*scenario*_base.txt file with actual key and token and save it as api_selector/*scenario*.txt
        replace_api_credentials(
            model="api_selector",
            scenario=scenario,
            actual_key=os.environ["TRELLO_API_KEY"],
            actual_token=os.environ["TRELLO_TOKEN"]
        )
        
        # Replace the key and token placeholders in planner/*scenario*_base.txt file with actual key and token and save it as planner/*scenario*.txt
        replace_api_credentials(
            model="planner",
            scenario=scenario,
            actual_key=os.environ["TRELLO_API_KEY"],
            actual_token=os.environ["TRELLO_TOKEN"]
        )

        query_example = "Create a new board with name 'abc_board'"
    
    elif scenario == "airtable":
        replace_api_credentials_in_json(
            ###to replace all the key and token variables in the specs file with real values
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["AIRTABLE_PERSONAL_ACCESS_TOKEN"]
        )
        api_spec, headers = process_spec_file(  ### to make the specs file minfy or smaller for for better processing
            file_path="specs/airtable_oas.json",
            token=os.environ["AIRTABLE_PERSONAL_ACCESS_TOKEN"]
        )

        # Replace the key and token placeholders in api_selector/*scenario*_base.txt file with actual key and token and save it as api_selector/*scenario*.txt
        replace_api_credentials(
            model="api_selector",
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["AIRTABLE_PERSONAL_ACCESS_TOKEN"]
        )
        
        # Replace the key and token placeholders in planner/*scenario*_base.txt file with actual key and token and save it as planner/*scenario*.txt
        replace_api_credentials(
            model="planner",
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["AIRTABLE_PERSONAL_ACCESS_TOKEN"]
        )

        query_example = "Display all jokes"
        
    elif scenario == "elevenlabs":
        replace_api_credentials_in_json(
            ###to replace all the key and token variables in the specs file with real values
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["ELEVEN_LABS_API_KEY"]
        )
        api_spec, headers = process_spec_file(  ### to make the specs file minfy or smaller for for better processing
            file_path="specs/elevenlabs_oas.json",
            token=os.environ["ELEVEN_LABS_API_KEY"]
        )

        # Replace the key and token placeholders in api_selector/*scenario*_base.txt file with actual key and token and save it as api_selector/*scenario*.txt
        replace_api_credentials(
            model="api_selector",
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["ELEVEN_LABS_API_KEY"]
        )
        
        # Replace the key and token placeholders in planner/*scenario*_base.txt file with actual key and token and save it as planner/*scenario*.txt
        replace_api_credentials(
            model="planner",
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["ELEVEN_LABS_API_KEY"]
        )

        query_example = "Generate speech from the text 'If a mum is short, do you call her mini-mum?'"
        
    elif scenario == "dalle3":
        replace_api_credentials_in_json(
            ###to replace all the key and token variables in the specs file with real values
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["AZURE_OPENAI_API_KEY"]
        )
        api_spec, headers = process_spec_file(  ### to make the specs file minfy or smaller for for better processing
            file_path="specs/dalle3_oas.json",
            token=os.environ["AZURE_OPENAI_API_KEY"]
        )

        # Replace the key and token placeholders in api_selector/*scenario*_base.txt file with actual key and token and save it as api_selector/*scenario*.txt
        replace_api_credentials(
            model="api_selector",
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["AZURE_OPENAI_API_KEY"]
        )
        
        # Replace the key and token placeholders in planner/*scenario*_base.txt file with actual key and token and save it as planner/*scenario*.txt
        replace_api_credentials(
            model="planner",
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["AZURE_OPENAI_API_KEY"]
        )

        query_example = "Generate a image that represent goes with the following joke 'If a mum is short, do you call her a mini-mum?'"
    
    elif scenario == "zerocodekit":
        replace_api_credentials_in_json(
            ###to replace all the key and token variables in the specs file with real values
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["ZERO_CODE_KIT_API_KEY"]
        )
        api_spec, headers = process_spec_file(  ### to make the specs file minfy or smaller for for better processing
            file_path="specs/zerocodekit_oas.json",
            token=os.environ["ZERO_CODE_KIT_API_KEY"]
        )

        # Replace the key and token placeholders in api_selector/*scenario*_base.txt file with actual key and token and save it as api_selector/*scenario*.txt
        replace_api_credentials(
            model="api_selector",
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["ZERO_CODE_KIT_API_KEY"]
        )
        
        # Replace the key and token placeholders in planner/*scenario*_base.txt file with actual key and token and save it as planner/*scenario*.txt
        replace_api_credentials(
            model="planner",
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["ZERO_CODE_KIT_API_KEY"]
        )

        query_example = "Save the file from 'https://www.metagineers.com/MetagineersLogo.png'"
        
    elif scenario == "resend":
        replace_api_credentials_in_json(
            ###to replace all the key and token variables in the specs file with real values
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["RESEND_API_KEY"]
        )
        api_spec, headers = process_spec_file(  ### to make the specs file minfy or smaller for for better processing
            file_path="specs/resend_oas.json",
            token=os.environ["RESEND_API_KEY"]
        )

        # Replace the key and token placeholders in api_selector/*scenario*_base.txt file with actual key and token and save it as api_selector/*scenario*.txt
        replace_api_credentials(
            model="api_selector",
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["RESEND_API_KEY"]
        )
        
        # Replace the key and token placeholders in planner/*scenario*_base.txt file with actual key and token and save it as planner/*scenario*.txt
        replace_api_credentials(
            model="planner",
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["RESEND_API_KEY"]
        )

        query_example = "Send a status update email 'Your joke assets are now ready.'"
        
    elif scenario == "zerocodekitcredit":
        replace_api_credentials_in_json(
            ###to replace all the key and token variables in the specs file with real values
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["ZERO_CODE_KIT_API_KEY"]
        )
        api_spec, headers = process_spec_file(  ### to make the specs file minfy or smaller for for better processing
            file_path="specs/zerocodekit_oas.json",
            token=os.environ["ZERO_CODE_KIT_API_KEY"]
        )

        # Replace the key and token placeholders in api_selector/*scenario*_base.txt file with actual key and token and save it as api_selector/*scenario*.txt
        replace_api_credentials(
            model="api_selector",
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["ZERO_CODE_KIT_API_KEY"]
        )
        
        # Replace the key and token placeholders in planner/*scenario*_base.txt file with actual key and token and save it as planner/*scenario*.txt
        replace_api_credentials(
            model="planner",
            scenario=scenario,
            actual_key="",
            actual_token=os.environ["ZERO_CODE_KIT_API_KEY"]
        )

        query_example = "Display how much credit is left."
        
    else:
        raise ValueError(f"Unsupported scenario: {scenario}")

    populate_api_selector_icl_examples(scenario=scenario)
    populate_planner_icl_examples(scenario=scenario)

    requests_wrapper = Requests(headers=headers)

    # Load the environment and the model and create an API LLM instance
    load_dotenv()
    
    # Choose your LLMs by assigning llm to one of the following
    
    # OpenAI API
    # llm_openai = OpenAI(model_name="gpt-4-turbo", temperature=0.0, max_tokens=2048)
    
    # llm_llama3 = Ollama(model="llama3", temperature=0.0, num_ctx=2048)
    # llm_phi3 = Ollama(model="phi3", temperature=0.0, num_ctx=2048)
    
    # DEFAULT for best performance AzureOpenAI API For OpenAI
    llm = AzureChatOpenAI(
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
        openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    )
    
    api_llm = ApiLLM(
        llm=llm,
        api_spec=api_spec,
        scenario=scenario,
        requests_wrapper=requests_wrapper,
        simple_parser=False,
    )

    print(f"Example instruction: {query_example}")
    query = input(
        "Please input an instruction (Press ENTER to use the example instruction): "
    )
    if query == "":
        query = query_example

    logger.info(f"Query: {query}")

    start_time = time.time()
    
    # Run the query via the api_llm instance
    api_llm.run(query)
    logger.info(f"Execution Time: {time.time() - start_time}")

if __name__ == "__main__":
    main()