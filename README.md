# Content Creator Acellerator - An Agile Loop Synapse Copilot Hackathon Entry

The [Synapse Copilot](https://synapse.agileloop.ai) is a tool that allows you to integrate Large Language Models (LLMs) with a wide array of APIs. 

## Background

I am a content creator and much of my work involved lots of repetitive tasks be it video creation or writing blogs and I have been looking for a way to automate some of these tasks. I find that Synapse Copilot is perfect starting point for creating a tool that can help me automate some of these tasks. It is still in early stages but it has potential to be a great tool for content creators. Joining the Agile Loop Hackathon is a great way to explore the possibilities of this tool.

## Scenario/Use Case

For the purpose of the Agile Loop Hackathon conducted via LabLab.ai I have narrowed down a scenario to a content creator who are looking to exploit the current trending virality of Dad Joke videos we see on YouTube, TikTok and Instagram. 

These Dad Jokes videos are extremely popular yet simple. They are usually short videos that are funny and can be easily created. The content creator can use Synapse Copilot to automate the process of creating these videos by generating the jokes, creating the video and posting them on the social media platforms.

## Anatomy of a Dad Joke Video

Most of the videos are simple one liners or two liners such as:

```If a child refuses to sleep during nap time, are they guilty of resisting a rest?```

It is usually a video of someone talking and telling the joke, pausing a little and then give the punchline. 

While we can possibly try to automate with Talking Avatars etc, which is very much possible nowadays. I am going to keep it simple and just assume it's a faceless video with just a simple picture that is related to the one liner being shown while a Deep Morgan Freeman kind of video plays in the background.

Also due to time constraint, as as the focus is more on the integration of the 5 different SaaS tools, I will not be creating the video but just the automation of the process of creating the assets needed for the video.

Also rather than let the AI (although it is an option) generate the OneLiner, I am assuming the joke will be given by the user.

## Automation Chain

The automation chain will be as follows:

1. Allow input from the user to start off with Dad Joke e.g. 'Create a new joke video with the joke "If a child refuses to sleep during nap time, are they guilty of resisting a rest?"'

2. The joke will cause an ```AirTable``` record to be created with the Joke and a status of Todo.

3. The one liner is then passed to ```ElevenLabs``` to generate the voiceover for the joke.

4. The one liner is the passed to ```Dalle3``` to generate an image that is related to the joke.

5. I also added a credit check with ```0Codekit``` to check if the user has enough credits to proceed (although this is working, ideally if the check is ok, we should be doing more tasks with 0CodeKit. OCodeKit have heaps of API endpoints and since they have the PostMan files, addded groups of features are very simple).

6. ```Resend``` an email sender api is then used to send an email to the user to let them know the assets are ready.

## Gotchas and Caveats

I will still need to glue up the above together and test it out. I have tested the individual scenarios and they are working fine. Ideally, once the joke has been entered, it's a fire and forget. The user will get an email once the assets are ready (or if there are any issues).

## Synapse Copilot Starter Kit

I used my own Synapse Copilot starter kit to kickstart this project. This starter kit is a fork of the original official repo at [https://github.com/Agile-Loop/Synapse-Copilot.git](https://github.com/Agile-Loop/Synapse-Copilot.git). It does not overwrite the original repository files and all additional files has a *_starter* prefix in the filename.

The starter kit fork of the original official repo can be found here. [https://github.com/goldzulu/Synapse-Copilot.git](https://github.com/goldzulu/Synapse-Copilot.git)

The main ReadMe File repo can be found here [README_starter.md](README_starter.md) file.

## Running the tool 

To run the tool, you can follow the initial steps contained in the [README_starter.md](README_starter.md) file with the obvious difference being the 5 New SaaS integration focused and working as far as I know for:

1. AirTable [https://airtable.com](https://airtable.com)
2. ElevenLabs [https://www.elvenlabs.com](https://www.elvenlabs.com)
3. Dalle3 [https://openai.com/index/dall-e-3/](https://openai.com/index/dall-e-3/) - via https://openai.com or https://azure.openai.com
4. 0Codekit [https://www.0codekit.com](https://www.0codekit.com)
5. Resend [https://resend.com](https://resend.com)

 The original Trello scenario has not been fully tested after the tweeks needed for the use case of this hackathon project.

You need to obtain the necessary keys for the above, all of which have placeholders in the config_starter.yaml file. or the .env.local (copy to .env and change config_starter.yaml to use_config_file: false if you go along the .env route).

```python run_starter.py``` will run the tool the first instructions being to enter the oneliner Joke.

### AirTable Setup

It is expected that you have an AirTable base called Jokes with columns Joke, Status, Image and Speech. The Image and Speech columns are for the image and speech generated by Dalle3 and ElevenLabs respectively.

# Future 

The intention is to provide an incremental tutorial as I add more feature as a sequel to the original video [Synapse Copilot Starter Tutorial](https://youtu.be/_ilJAjcGjvM) that helps you to quickly understand the project structure by running an example scenario and later on perhaps a way to create your own scenario.

I have also a bigger automation project called project Davinci, that uses a graphical flow builder to setup automation tasks for content creator. Potentially I might integrate it to Synapse Copilot as well.

Please open up a github issue to this repository or put some comments on the YouTube video and let me know what you think.

You can also follow me on X at [@voicetechguy1](https://x.com/voicetechguy1).