# decentralized-electronic-health-record
A decentralized electronic health record. Get ahead of the virus by tracking symptoms, geolocation and social connections while protecting patient privacy.

## Goal:
The goal is to build a decentralized EHR that looks for symptoms of COVID-19 and helps with reducing the transmission rate.

## See how to organize a hackathon project:
[How we will organizing team and project.](https://medium.com/linnia/how-to-organize-a-project-in-a-hackathon-be54f167498a)


## Understanding the problem: 
1. Understood the domain
2. Agreed on a problem within that domain
3. Deeply understood the problem after some discussion. 
4. The team agrees that it is a real problem worth addressing.

**Domain**: COVID-19.
See the CDC's information on Coi

**Problem**: COVID-19 is a pandemic which need mitigating. 

Social distancing to reduce case load on healthcare system is the method chosen by governments. Here are [some terms to know] (https://www.nytimes.com/2020/03/11/science/coronavirus-terms-to-know.html)

**Understanding the problem**: Check out the [issue](https://github.com/COVID-19-electronic-health-system/decentralized-electronic-health-record/issues) and (Discord server)[https://discord.gg/BEz3Eb] to ask questions and see discussions.

**Agree that its a problem**:  
We can agree that COVID-19 is a problem and that mitigating its effects would be worthwhile.

How to address mitigate it effectively?

## Why are design statement important:
Design statements are a north star to keep the team focused on the problem.

## Crafting Design Statement:
1. What problem(s) are we solving?

- Mitigating the spread of COVID-19 to avoid overwhelming the healthcare system. 

- Helping older invidiuals avoid public areas to reduce their chances of infection.

- **Anything else?** Post an [issue](https://github.com/COVID-19-electronic-health-system/decentralized-electronic-health-record/issues) to see what is most effective to tackle on. 

2. Who is the user that is suffering real pain from the problem?
- Everyone. However, in order of severity: Older people, people with immune system issues, older smokers. 

3. What will the situation look like for the user when the user’s problem is addressed?
- [A flatter curve](https://www.nytimes.com/2020/03/11/science/coronavirus-curve-mitigation-infection.html); Less transmissions translating to lower caseload for hospitals. This means more ventilators and staff per person. The idea is to spread out the infections (or for vunverable population, avoid them all together while healthy population gains 'herd immunity').

- Ideally, the numbers in US per thousand will be lower than Italy or China.

## Design statement:  
How might we improve _(problem in the domain)______ for _(user)___ , so that _(user-focused outcome)______?

How might we improve **lowering the transmission rate** for **TARGET_POPULATION**, so that we can **flatten the curve on the healthcare system** and **avoid possible infection**?

We must decide on who is our **TARGET_POPULATION**

Is it elderly?  
Is it adults with immune system deficiencies?  
Is it the general population?   Will be too broad?

Open an [issue](https://github.com/COVID-19-electronic-health-system/decentralized-electronic-health-record/issues) to discuss.

## Discord server
Join our discord server:
https://discord.gg/BEz3Eb

## IPR- Initial Public Release Features
There will be three features
1) Symptom tracker that follows a specific medical protocol.   
Help needed from medical professionals.

2) Geolocation  
Help needed from devs with Geolocation experience

3) Social network  
Help needed to create a system that maps connections, but respects privacy. Maybe just hashed phone number or something as an ID.

We want to help generate data so that researchers can learn from the data real-time (while respecting privacy).

## Tech Stack:
?- open for debate. Post in [issue](https://github.com/COVID-19-electronic-health-system/decentralized-electronic-health-record/issues).

Front end:   
React, Redux (?), React-Router, 

Geolocation:
JavaScript Geoloation API, MapBox(?)

Design System:  
react-boostrap (?)

Back end:  
ExpressJS, NodeJS, MongoDB (?)

## Wireframes:
In progress.

So far we need:
1. Sign in screen
2. some sort of auth flow. Maybe OAuth.   
Perhaps Google and Facebook since it has wide coverage. Later Twitter.
3. Map screen
4. Survey flow. Perhaps something. Like swiping left or right for yes or no related to questions.

## Medical Questions to ask:
In Progress.  
Open an [issue](https://github.com/COVID-19-electronic-health-system/decentralized-electronic-health-record/issues).

## Privacy 
In Progress.
Thinking of using [Blockstack](https://docs.blockstack.org/) and using [Sundly](https://github.com/Sundly) as inspiration.

Blockstack allows for users to own their data in a decentralized manner. 

They also have a encrypted centralized sever called [Radiks](https://github.com/blockstack/radiks) which we can used to build model-driven decentralized applications. 

Open an [issue](https://github.com/COVID-19-electronic-health-system/decentralized-electronic-health-record/issues) to suggest ideas. Open to all ideas.

Is a regular expressJS/NodeJS server hosted on Heroku better?

## Looking for:
React Developers  
React Native Developers  
Medical Professionals  
Health informatics professionals  
Devs with experience using FHIR   
Epidemiologists  
System biologists  
Data scientists  
Designers  
UX/UI  
Project managers  

Translators:   
Korean, Chinese, Persian, Spanish, Portuguese, French, German, Russian, you name it.

And you.

Open up an [issue](https://github.com/COVID-19-electronic-health-system/decentralized-electronic-health-record/issues). And let's try to stem this before it gets more significant than it is.

## Progress:
As of March 12th, 2020:
Assembling team. 
See [organization members](https://github.com/orgs/COVID-19-electronic-health-system/people).

As of March 13th, 2020:  
Scoping out features for Initial Product release. 

Decided on Progressive Web App using React. 

Spoke with the maintainer of [Sundly](https://github.com/Sundly/sundly/issues/22), an EHR created on Blockstack. It has plenty of code. Willing to help and let us and let us use/maintain the code.

On March 13th, 2020, @6:30pm:
Will speak with Emergency room doctor and system architect with experience in medical workflows.


## Priorities:
**Ideally, we should be able to launch something by Monday afternoon (March 16th, 2020)**

As of March 13th, 2020:
1) The main priority is to narrow down features that experts will find useful. 

2) Then we can scope out features. Then create simple wireframes to build out front end. 

3) Then we can start to assign work and build.

4) Get a domain name and launch.
It should be sharable by text or WhatsApp.

Target is to have features scoped out by tonight. Start assigning features and work by Saturday morning. 