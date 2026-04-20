# 1. Team Identity

## 1.1 Studio / Group Name
`[Enter your group name]`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
|`Mishka Bhandary` | `Coding` | `Electronics & Troubleshooting` | `Circuit connections, breadboard wiring, debugging` |
|`Devina Jha` | `Fabrication & Mechanics` | `Troubleshooting` | `Physical build, ideation sketches, repository setup` |

## 1.3 Project Title
`A Capacitive Touch Rhythm Controller Built on ESP32 Hardware with Real-Time Browser Game Integration`

## 1.4 One-Line Pitch
`We engineered a floor-based, 4-column capacitive touch controller using an ESP32 microcontroller and aluminum foil pads that you physically step on to play Magic Piano Tiles in real time, with zero lag and maximum chaos.`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`This project is a fully custom-built human-input device (HID) that hijacks a browser-based rhythm game using nothing but an ESP32, some wire, and aluminum foil. The ESP32 has built-in capacitive touch pins that detect when a conductive surface makes contact with a person.` 

`Each pin is wired to a strip of aluminum foil laid flat on the floor as a step pad. We built 4 columns to match the exact lane layout of Magic Piano Tiles, so when you step on a pad, the board picks up the change and fires the corresponding input to the game running in the browser. We had to manually tune the sensitivity on each pad to handle the force and contact area of a foot rather than a fingertip, filter out ghost triggers, and deal with the general chaos of conductive pads on the floor, which is a lot trickier than it sounds.`

`The real challenge was making it consistent and fast enough to keep up with tiles at full speed. That meant writing tight polling loops, adding debounce logic to avoid double-inputs, and arranging the 4 pads in a layout that felt natural to actually play with your feet. The final result is something that looks unconventional but performs like a piece of real hardware engineering, which is exactly the point.`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`What is the experience:
We built a physical floor controller from scratch and connected it to a game that already has people in a chokehold. You are not tapping a screen anymore, you are stepping on actual foil pads that we wired, coded, and calibrated ourselves, laid out in 4 columns to match the game exactly. The browser has no idea you are playing it with your feet.`

`What do you want the player or participant to feel:
We want them to feel the exact same spiral we felt building it, that mix of frustration when something is not working and then the rush when it clicks. Piano Tiles already does that on its own but now your whole body is involved. You are standing, stepping, trying not to lose your balance while the tiles get faster. We want them to panic, mess up, laugh about it, and immediately want another go.`

`Why would someone want to try it again:
Piano Tiles does not let you walk away clean. You will always miss a step and need to prove to yourself you can do better. But with our controller there is an extra layer because you are also getting used to the pads, figuring out your footing, and quietly trying to outlast whoever played before you. It turns into a competition without anyone officially declaring one.`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`We are designing this project as if we are a small creative studio making a playable object for classmates and exhibition visitors who want to experience something familiar in a way they have never physically interacted with before.`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `Website` | `https://randomnerdtutorials.com/esp32-touch-pins-arduino-ide/` | `This showed us that aluminum foil wired to an ESP32 touch pin is a legitimate way to build a touch pad. It confirmed that the sensitivity thresholds we needed to tune were real and documented, not something we were making up as we went.` |
| `App` | `https://magictiles.org` | `The game was the whole reason the project exists. We wanted to see if we could make it playable on physical pads and whether the hardware could actually keep up with the speed of the tiles.` |
| `Video` | `https://www.youtube.com/watch?v=nXjj9IXUaA4` | `This video showed us that you can build a physical game controller using an Arduino and basic hardware that connects directly to a game. Seeing someone turn a DIY pad into a fully functional DDR controller made us confident we could do the same thing with piano tiles and an ESP32.` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`Most people have played Piano Tiles on a phone screen. We pulled it off a screen entirely and rebuilt the input layer from scratch using an ESP32 and 4 aluminum foil pads laid out on the floor that you step on to play. There is no kit for what we made. We figured out the touch sensitivity thresholds for foot contact, solved the signal noise issues, and got it responsive enough to actually keep up with the game at full speed.`

`The twist is that the controller looks unconventional but performs like something engineered, and the game it connects to is one people already have a history with, so the moment they step on the pads it feels both familiar and completely new.`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`step → sensor detects → keystroke fires → tile registers → miss or survive → step again`

`The loop is fast, physical and unforgiving. The game dictates the pace and your feet have to keep up. Every correct step keeps you in, every missed pad ends the run and sends you straight back to try again.`



## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `Classmates, exhibition visitors, anyone who has played Piano Tiles before and wants to experience it in a completely different way` |
| Age range | `9 and up` |
| Solo or multiplayer | `Solo, but with an audience watching and waiting for their turn which makes it competitive anyway` |
| Expected duration of one round | `30 seconds to 2 minutes depending on how far you get before you miss` |
| What should the player feel? | `Panicked, focused, slightly ridiculous, and desperate to go again` |
| Is explanation required before use? | `Minimal. Step on the pad that matches the falling tile. Most people figure it out in the first 10 seconds.` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `They see a floor mat made of 4 aluminum foil pads laid out in columns with a screen showing Magic Piano Tiles running above it. Someone is probably already playing or just finished, which is what draws them in.`
2. **Start:** `They step up to the mat and stand behind the 4 pads, one foot ready. No login, no setup, the game is already running.`
3. **First Action:** `They step on whichever pad matches the first falling tile and immediately feel whether it registered or not.`
4. **Main Interaction:** `Tiles fall in one of 4 columns and they have to step on the matching pad in time, continuously, while the speed increases the longer they survive.`
5. **System Response:** `The ESP32 picks up the step, fires the keystroke to the browser, and the game registers the tile hit in real time. If the pad is missed or a white tile is stepped on, the game ends immediately.`
6. **Win / Lose / End Condition:** `The round ends when they miss a tile or step on a white space. Their score shows on screen.`
7. **Reset:** `The game resets in one click and the next person steps up.`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `Step only on the pad that matches the falling black tile, one column at a time`
- `Stepping on a white tile or missing a black tile ends the round immediately`
- `One player at a time on the mat`
- `You cannot use your hands, feet only`

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] `All 4 foil pads reliably detect a foot step and send the correct keystroke to the browser without false triggers or missed inputs`
- [ ] `The game runs in the browser and responds to the ESP32 input in real time with no noticeable lag`
- [ ] `A full round can be played from start to game over without the system crashing or disconnecting`
- [ ] `The pads stay in place during play and do not shift or lose contact under the pressure of being stepped on`
- [ ] `A new player can pick it up and understand how to play within the first 20 seconds without being explained anything`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`4 foil pads on the floor, wired to an ESP32, connected to a laptop running Magic Piano Tiles in a browser. Steps register as keystrokes and the game responds. That is the whole thing and it already works`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `A scoreboard that tracks and displays the top scores across multiple players during an exhibition`
- `A custom enclosure or frame around the pads to make the mat look more polished and keep everything in place during heavy use]`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

[✓] Electronics-based

[✓] Mechanical

[✓] Sensor-based

[✓] App-connected

[•] Motorized

[•] Sound-based

[•] Light-based

[✓] Screen/UI-based

[✓] Fabricated structure

[✓] Game logic based

[✓] Installation / tabletop experience

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`[Write here]`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `Aluminum foil pads (x4)` | Input | `Detects when a foot steps on the pad and sends the signal to the ESP32 via capacitive touch pins` |
| `ESP32 / Controller` | Processing | `Reads the touch input from each pad, applies sensitivity thresholds and debounce logic, then fires the corresponding keystroke to the browser` |
| `Browser / Magic Piano Tiles` | Output | `Receives the keystroke, registers the tile hit, and updates the game state on screen in real time` |
| `4-column floor mat assembly` | Physical Action | `Player stands on the mat and steps on the pad matching the falling tile, driving the entire input chain with their foot` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[30 inches]` |
| Width | `[11 inches]` |
| Height | `[3 inches]` |
| Estimated weight | `[1-2kgs]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

[•] Gears

[•] Pulleys

[•] Belt drives

[•] Linkages

[•] Hinges

[•] Shafts

[•] Springs

[•] Bearings

[•] Wheels

[•] Sliders

[•] Levers

[✓] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`There is no traditional mechanism in this project. The physical structure is 4 aluminum foil pads laid flat on the floor in a column layout. The only mechanical interaction is a foot pressing down onto a pad, which brings the foil into firm enough contact to be detected by the ESP32's capacitive touch pin. The construction is intentionally simple because the complexity lives in the electronics and firmware, not the physical assembly.`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`The only thing that moves is the player's foot coming down onto the pad. The foot pressing down causes the movement. The distance is just however far a natural step travels, a few centimeters at most. The speed depends entirely on how fast the player is reacting to the tiles, which at high game speeds gets very fast. What could go wrong is the pad sliding across the floor mid-game from repeated stepping, the foil bunching up and losing flat contact, or the wire pulling loose from the pad if a step lands on the connection point rather than the center of the foil.`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `Not Applicable` | `Not Applicable` | `Not Applicable` |
| `Not Applicable` | `Not Applicable` | `Not Applicable` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`Not Applicable`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `ESP32` | `1` | `Main controller` |
| `Aluminum Foil Pads` | `4` | `Act as the conductive touch surface that detects when a foot steps on them` |
| `Jumper Wires` | `8` | `Connect each foil pad to the corresponding capacitive touch pin on the ESP32` |
| `USB Cable` | `1` | `Powers the ESP32 and maintains the serial connection to the laptop` |
| `Laptop / Computer` | `4` | `Runs Thonny for firmware, hosts the browser running Magic Piano Tiles` |
| `Breadboard` | `1` | `Organizes and stabilizes the wiring connections on the ESP32` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`Each aluminum foil pad is connected via a jumper wire to one of the ESP32's capacitive touch GPIO pins. There are 4 pads and 4 dedicated touch pins, one per column. All grounds are connected through the breadboard. The ESP32 is powered and communicates with the laptop via USB. The MicroPython firmware running in Thonny continuously polls each touch pin, checks the reading against a set threshold, and when a step is detected it sends the mapped keystroke to the browser.`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[https://www.figma.com/design/FKTekB9UcHeT6a4AJiR0C5/Images?node-id=3-61&p=f&t=iF5ayZWNHopUMEsI-0]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `USB connected to laptop` |
| Voltage required | `5V via USB` |
| Current concerns | `Minimal, the ESP32 and capacitive touch pins draw very little current and the foil pads are passive conductors with no power running through them directly` |
| Safety concerns | `No high voltage involved. The only risk is a loose wire pulling out mid-game which would cause a pad to stop responding, not cause any harm` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `Thonny IDE` | `Writing, uploading and debugging the MicroPython firmware on the ESP32` |
| `MicroPython` | `The firmware language running on the ESP32 that handles touch detection, threshold logic and keystroke output` |
| `Browser (Chrome / any)` | `Runs Magic Piano Tiles and receives the keystrokes fired by the ESP32` |
| `Magic Piano Tiles (web)` | `The game itself, the target application the controller is built to play` |


## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`When the program starts, it sets up a BLE keyboard called “ESP32” and connects four touch sensors to pins 15, 13, 12, and 14, mapped to keys F, G, H, and J. It then runs a calibration step, taking multiple readings from each sensor to find their normal (resting) values. After printing these values, it waits until a Bluetooth connection is made.
Two methods are used for reading sensors. During calibration, 50 readings are taken and averaged. During normal use, 10 quick readings are averaged to reduce noise while keeping the system responsive.
In each loop, all four sensors are read. The program compares the current value to the baseline to calculate a delta. A drop in value means the sensor is being touched. To avoid flickering, the system uses hysteresis. A key is pressed when the delta is above 20, and released when it drops below 10. A 200ms delay prevents rapid repeated inputs. The program keeps track of whether each key is currently held.
All active keys are sent together as a single keyboard signal via Bluetooth. This allows multiple keys to be pressed at once. Key actions (like “F DOWN” or “H UP”) are also printed for debugging.
The program constantly checks if Bluetooth is connected. Once connected, it waits 2 seconds before sending inputs to ensure stability. Inputs are only sent while connected. If the connection is lost, all keys are reset to avoid stuck inputs. The system also slowly adjusts the baseline values over time when no keys are pressed, helping maintain accuracy despite environmental changes like temperature or humidity.`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[(https://www.figma.com/design/FKTekB9UcHeT6a4AJiR0C5/Code-Flowchart?node-id=0-1&t=iF5ayZWNHopUMEsI-1)]`

## 10.4 Pseudocode

```text
[START

Setup BLE keyboard
Setup 4 touch sensors (F, G, H, J)

Calibrate sensors → store baseline values

WAIT until Bluetooth connects

LOOP forever:

    IF connected:

        Read all sensors
        Compare each reading with its baseline

        IF value change is high → key is pressed
        IF value returns to normal → key is released

        Apply debounce (ignore very fast repeats)

        Track which keys are currently held

        Send all active keys to laptop

        IF no keys are pressed:
            slowly update baseline (adjust for environment)

    ELSE:
        Reset all key states

    Wait a short time

END LOOP]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
[•] Yes
[✓] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`Not Applicable`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `[Spec]` | `[Enables wireless keyboard input and touch sensing in one board]` |
| `[Plywood Board (30 × 11 inch)]` | `[1]` | `[No]` | `[No (obtained from lab)]` | `[0]` | `[30 × 11 inch]` | `[Provides a strong, stable base for stepping and mounting components]` |
| `[Aluminum Foil]` | `[1]` | `[No]` | `[Yes]` | `[74 INR]` | `[1 roll]` | `[Acts as conductive material for capacitive touch sensors]` |
| `[Jumper Wires]` | `[10]` | `[Yes]` | `[No]` | `[0]` | `[10 wired]` | `[connection between tiles and ESP32 pins]` |
| `[A3 Paper]` | `[1]` | `[No]` | `[Yes]` | `[200 INR]` | `[140 GSM Sketchbook]` | `[Layered ontop of aluminium for better gameplay]` |
| `[Electrical Tape]` | `[1]` | `[No]` | `[Yes]` | `[100 INR]` | `[4 rolls]` | `[Secures components and prevents short circuits]` |
| `[Super Glue]` | `[1]` | `[No]` | `[Yes]` | `[50 INR]` | `[Fast-setting adhesive]` | `[Strong bonding for fixing layers and components]` |
| `[Wooden Strips]` | `[5]` | `[No]` | `[Yes]` | `[0]` | `[Narrow wooden battens]` | `[Reinforces board to prevent bending and breaking during use]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[The materials and components were selected based on a balance of durability, simplicity, cost, and suitability for rapid prototyping. Plywood was chosen for the base instead of cardboard because it provides the strength and rigidity needed to withstand repeated stepping without bending or damage. Aluminum foil was used for the touch sensors due to its high conductivity, low cost, and ease of shaping, making it more practical than specialized conductive materials. A layered paper structure was preferred over more complex mechanisms because it allowed quick experimentation with sensitivity and responsiveness.The ESP32 was selected because it integrates capacitive touch sensing and Bluetooth connectivity in a single board, reducing the need for additional components and simplifying the system. Capacitive touch sensing was used instead of mechanical switches to avoid moving parts, making the tiles thinner, quieter, and less prone to wear. Electrical tape and super glue were chosen for fastening as they are quick to apply, flexible, and sufficient for a prototype, unlike screws or permanent fixtures which would make iteration harder. Overall, the choices prioritized ease of fabrication, quick iteration, and reliable performance, allowing the project to be developed and refined efficiently within the given time.]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[Aluminum Foil]` | `[conductive material for capacitive touch sensors]` | `[(https://www.zepto.com/pn/hindalco-fresh-wrapp-aluminium-foil-9-m/pvid/635e63a4-d665-4a28-b6b5-79da5bd6ad72)]` | `[10/04/2026]` | `[Received]` |
| `[Electrical Tape]` | `[Secure components and prevent short circuits]` | `[(https://www.zepto.com/pn/abk-multicolour-high-performance-electric-insulation-tape-18-mm-x-6-m-pack-of-5/pvid/dddd3ab7-e7d3-4a94-b83a-959e91fd2bc0)]` | `[10/04/2026]` | `[Received]` |
| `[Super Glue]` | `[Strong bonding for fixing layers and components]` | `[(https://www.zepto.com/pn/fevikwik-gel-instant-glue-for-repair-no-spillage-clear-non-drip-formula-extra-repair-time/pvid/067d5ac6-1335-4658-9b2d-c866b7ec515b)]` | `[10/04/2026]` | `[Received]` |
| `[A3 Paper]` | `[Layered ontop of aluminium for better gameplay]` | `[(https://www.amazon.in/Camel-140-Sketch-Book-Pages/dp/B0CZS143FV?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A1WLX31ILRWLJY)]` | `[13/04/2026]` | `[ordered]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[0]` |
| Mechanical parts | `[0]` |
| Fabrication materials | `[464]` |
| Purchased extras | `[100]` |
| Contingency | `[50]` |
| **Total** | `[614]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[Not Applicable]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`The team divided tasks based on individual strengths to work efficiently. Mishka focused on coding, electronics, and debugging, including sensor calibration and Bluetooth communication. Devina handled fabrication and mechanical aspects, such as building the board, assembling the tiles, and refining the physical layout. Both members collaborated on troubleshooting and testing, especially where hardware and software overlapped.
Decisions were made collaboratively through discussion and quick testing. Instead of long planning phases, the team relied on building and testing small changes, then choosing the option that performed best in practice. Progress was checked regularly through testing sessions after each build or code update. Each iteration was evaluated based on responsiveness, usability, and stability, ensuring continuous improvement.
Documentation was maintained alongside the process. Key changes, test results, and issues were recorded after each session, including version updates and debugging logs. This ensured that progress was tracked clearly and decisions could be justified in the final report.
`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Mishka + Devina]` | `2` | `[30/03/2026]` | `None` | `Done` |
| T2 | `[Complete BOM]` | `[Devina]` | `1` | `[06/04/2026]` | `T1` | `Done` |
| T3 | `[Test electronics]` | `[Mishka]` | `2` | `[10/04/2026]` | `T1` | `Done` |
| T4 | `[Build structure]` | `[Devina]` | `3` | `[10/04/2026]` | `T1` | `Done` |
| T5 | `[Write control code]` | `[Mishka]` | `2` | `[12/04/2026]` | `T3` | `Done` |
| T6 | `[Integrate system]` | `[Mishka]` | `2` | `[15/04/2026]` | `T4, T5` | `Done` |
| T7 | `[Playtest]` | `[Mishka + Devina]` | `2` | `[17/04/2026]` | `T6` | `Done` |
| T8 | `[Refine and document]` | `[Mishka + Devina]` | `4` | `[20/04/2026]` | `T7` | `Done` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Devina + Mishka]` | `[None]` |
| Electronics | `[Mishka]` | `[Devina]` |
| Coding | `[Mishka ]` | `[Devina]` |
| App | `[Mishka]` | `[Devina]` |
| Mechanical build | `[Devina]` | `[Mishka]` |
| Testing | `[Devina+ Mishka]` | `[None]` |
| Documentation | `[Devina]` | `[Mishka]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [ ] Idea finalized
- [ ] Core interaction decided
- [ ] Sketches made
- [ ] BOM completed
- [ ] Purchase needs identified
- [ ] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [ ] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [ ] Physical body built
- [ ] Electronics integrated
- [ ] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 2 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 3 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[EBluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Reconnect logic + test before each session]` | `[Mishka]` |
| `[Structure breaks during play]` | `Mechanical` | `Low` | `High` | `[Reinforce base with wooden supports]` | `[Devina]` |
| `[Inconsistent touch sensitivity]` | `[Technical]` | `[Medium]` | `[High]` | `[Calibrate thresholds for each tile]` | `[Mishka]` |
| `[Wires disconnect during gameplay]` | `[Mechanical]` | `[Medium]` | `[High]` | `[Secure wiring with tape/glue]` | `[Mishka]` |
| `[Mismatch of tile selection and gampelay result]` | `[Gameplay]` | `[Low]` | `[Medium]` | `[Adjust tile spacing and layout]` | `[Devina]` |


## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`The biggest uncertainty at this stage is the **consistency and reliability of the touch input during real gameplay conditions**. While the system works in controlled testing, factors like different stepping pressure, player movement, and material wear can cause missed or false inputs. Ensuring that each tile responds accurately and consistently across different users and speeds remains the key challenge.`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Touch Pin Sensor]` | `[Attach to ESP32 and run a test code to see if they detect touch]` | `[Touch Pin detects touch]` |
| `[BLE Keyboard]` | `[Upload onto ESP32]` | `[When touching the touch pin results in the coressponding key being pressed on the keyboard]` |
| `[Touch Pad]` | `[Using aluminium foil sheets]` | `[The touch sensor is magnified across the aluminium pad and the pad can detect touch]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[give minimal instructions and see if they step on tiles correctly within 10–15 seconds]` |
| Is the interaction satisfying? | `[Ask for immediate feedback after 1 round (“Did it feel responsive/fun?”) and watch facial reactions/body movement]` |
| Do players want another turn? | `[Count how many players voluntarily replay without prompting]` |
| Is the challenge balanced? | `[Track the fail time, if its too fast the game is too hard, and too long meanstoo easy. Also ask “too easy / too hard / just right?”]` |
| Is the response clear and immediate? | `[check screen delay]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[06/04/2026]` | `[Inconsistent sensitivity between different touch pins]` | `[Technical]` | `[Calibrated touch values for each pin and set a threshold]` | `[Worked]` | `[None]` |
| `[10/04/2026]` | `[Steps sometimes don’t register when pressed lightly]` | `[Technical / Mechanical]` | `[adjusted touch sensitivity threshold in ESP32]` | `[Partly]` | `[Calibrate it to detect pressure with another layer over the touch pad]` |
| `[11/04/2026]` | `[Cable connections loosen during gameplay]` | `[Mechanical]` | `[Taped wires to board]` | `[Worked]` | `[None]` |
| `[15/04/2026]` | `[Touch isnt registered when placing a paper cover over the touch pad]` | `[Technical]` | `[Added a layer of aluminium foil to the bottom of the paper ]` | `[Partly]` | `[Change calibration in the code to make allowance for the Paper covering the touch pad]` |
| `[19/04/2026]` | `[Neopixel strip wont connect to the power supply and work]` | `[Mechanical]` | `[Changed the power supply and edited code]` | `[Failed]` | `[Unable to apply to board]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `friend (non-gamer)` | `[Rested foot on tile between steps]` | `Game triggered unintentionally` | `Slow-paced songs` | `Add to gameplay instructions not to rest on one tile between steps` |
| `Peer (non-gamer)` | `[Hesitated at start, looked at feet before stepping]` | `Didn’t understand tile-to-key mapping immediately` | `Found stepping interaction fun after a few tries` | `Add clear visual cues of piano tiles` |
| `Friend (gamer)` | `[Played confidently]` | `Timing felt slightly off during faster notes` | `Physical engagement made it more immersive` | `Increase pressure sensitivity to during faster notes it detects touch faster` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`The project was built as a full-scale interactive floor controller using simple materials, iterative prototyping, and embedded electronics. The keyboard structure was constructed from a 30 × 11 inch plywood board, reinforced with four wooden strips fastened along the perimeter and an additional central strip to improve stability during use. The surface was then divided into four equal sections, and aluminum foil sheets measuring 6 × 10 inches were cut to form consistent sensor pads. Each tile was assembled by layering a base conductive foil layer, a secondary foil layer, and a top contact layer made of paper, carefully aligned to ensure reliable triggering when stepped on. These tiles were arranged linearly on the board to correspond with the game inputs. Components were secured using electrical tape and super glue to maintain durability under repeated use. Each tile was wired to a capacitive touch pin on the ESP32 using jumper wires, with a common ground established where necessary. The microcontroller was programmed to convert each tile input into keyboard signals (F, G, H, L), enabling seamless interaction with the Piano Tiles game on a laptop via Bluetooth. The system was refined through multiple iterations based on testing, including adjustments to sensitivity in code to reduce false or missed inputs, modifications to tile spacing and layout for improved balance and comfort, and reinforcement of wiring after initial failures during active gameplay.`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[10/04/2026]` | `Built initial prototype using plywood base, foil touch sensors, and basic ESP32 input mapping` | `To test core concept of controlling Piano Tiles using foot interaction` |
| `v2` | `[13/04/2026]` | `Adjusted touch sensitivity and improved wiring stability` | `Initial testing showed missed inputs, false triggers, and confusion about tile mapping` |
| `v3` | `[19/04/2026]` | `Added secondary paper layer with aluminium foil for better responsiveness, modified tile spacing, and optimized code for reduced delay` | `To improve gameplay comfort, reduce input lag, and make interaction more reliable during fast sequences` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`The final outcome is a fully functional, interactive floor-based controller that allows users to play Piano Tiles using physical movement instead of traditional touch input. Built on a reinforced plywood base, the system uses four capacitive touch tiles made from layered aluminum foil and paper, each mapped to specific keyboard inputs (F, G, H, L). These inputs are processed by an ESP32 microcontroller and transmitted via Bluetooth to a laptop, enabling real-time gameplay. The design emphasizes full-body engagement, transforming a screen-based tapping game into an immersive, movement-driven experience. Through iterative prototyping, the system was refined for improved responsiveness, stability, and usability, resulting in a reliable and engaging interactive setup.`

## 18.2 What Works Well
- `The physical interaction is highly engaging and makes gameplay more immersive than standard touch controls`
- `The system successfully translates foot input into accurate keyboard signals with minimal delay`
- `The modular tile design allows for easy adjustments and experimentation with layout and spacing`

## 18.3 What Still Needs Improvement
- `Sensitivity can still vary slightly between tiles, affecting consistency`
- `Fast-paced gameplay is limited by physical movement speed and reaction time`
- `The current build could be more durable and refined for long-term or repeated use`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`The overall concept of the project remained largely unchanged from the initial plan, which was to create a floor-based controller for playing Piano Tiles. Most of the development focused on experimenting with different ways of constructing the touch pads to achieve reliable input. This included testing various material layers, arrangements, and sensitivity settings to improve consistency and responsiveness. Rather than significantly altering the design direction, the process was primarily iterative, refining the touch mechanism and physical build while keeping the original idea intact.`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`The team worked well in collaboratively building and testing the prototype, with tasks divided between fabrication, wiring, and coding. Communication was consistent during hands-on work, which helped in quickly identifying and fixing issues. However, progress was sometimes slowed down by trial-and-error, especially while figuring out the most reliable way to construct the touch pads and calibrate sensitivity. Time management was generally effective during building phases, but more structured planning earlier on could have reduced repeated iterations. Overall, responsibilities were shared fairly, and the team adapted well to challenges as they arose.`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`Through this project, we learned how capacitive touch sensing works in practice and how material choices and layering directly affect input reliability. In coding, we gained experience in mapping sensor inputs to keyboard outputs and optimizing responsiveness by adjusting thresholds and delays. Mechanically, we understood how small construction details, such as spacing and pressure distribution, influence performance. In terms of fabrication, we learned the importance of precision and durability when building interactive systems. Integration was a key learning area, as combining hardware, software, and physical interaction required constant testing and adjustment to ensure all components worked seamlessly together.`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`This project highlighted the importance of designing for play by focusing on engagement and physical interaction rather than just functionality. We learned that delight comes from the novelty of movement-based gameplay, but it must be supported by clarity in how the system works. Clear mapping between tiles and inputs was essential for player understanding, especially for first-time users. Iteration played a major role in improving the experience, as repeated testing revealed issues with balance, responsiveness, and usability. Overall, the project reinforced that good interaction design must consider both the physical and cognitive experience of the user.`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`With an additional week, we would focus on refining the build quality and user experience. This would include making the tiles more durable and consistent, improving sensitivity calibration across all inputs, and enhancing the overall finish of the board. We also struggled with sourcing LED strips, and would have liked to add LED strips that react to the touch sensors and flash multicoloured lights during the gameplay.`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [✓ ] Team details are complete
- [ ✓] Project description is complete
- [✓ ] Inspiration sources are included
- [ ✓] Player journey is written
- [✓ ] Sketches are added
- [✓ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
