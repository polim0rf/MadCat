# MadCat

### SYNOPSIS
  Tool used for speeding up IR operations
  

### DESCRIPTION

 Every Incident Response Analyst would confirm that the amount of tasks and services that need to be checked in order to investigate a particular event, incident, malicious file, suspicious url, etc. is huge. MadCat Tool is an attempt to automate the majority of tasks that an analyst performs on a daily basis, simplifying everything to the minimum. 
 
 The goal is to have a tool to drag-&-drop a suspicious file or string (URL/Hash) into MadCat and leave it to do every configured task for us (Submissions to AV services, retrieval of scan reports, etc.)
 

### ROADMAP

 - [ ] Add services/plugins (multi-scan engines submissions) 
 - [ ] Add plugin manager
 - [ ] Add a config file for services to be used by IR Analyst
 - [ ] Add installer/requirements
 - [ ] Improve Hasher
 - [ ] Improve Error Handling (currently inexistent)
 

### PARAMETERS 

    - Parameters should be optional, as the goal is to have the config file set up in advance, and have MadCat to do everything for us with a simple drag-&-drop action.


### NOTES

  - Version:        0.1.1
  - Author:         polim0rf
  - Creation Date:  16.10.2018
  - Purpose/Change: Initial script development (POC)


### EXAMPLES

 * Just drag-&-drop the suspicious file into MadCat
