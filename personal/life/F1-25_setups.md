---
title: F1-25_setups
author: Wynand Gouws
date: 2026-02-08 14:09:09
public: false
---

## Upgrade order

* Engine power
* Car weight
* Drag reduction
* ERS system

Then focus all on one category until it is done:

* Aero
* Powertrain
* Durability

* Partswap
  * at ~60%
  * 24/4 = 6 races
  * 24/2 = 12 races

## F1 setups

All tweaked by me, some of them are crap

### Australia

* black, black-, black+red, black, black+100, red
* R 28.5 24.5 22
* aero 20 25
* heavy undercut
  * 22s pit
  * start on softs, hards are very good
* overtake orange on corners 9 and 11
* speed green

### China

* L50, red, inside-red-minus, red, final-dhl-sign-minus, final sign
* Pressures 26, 27.5, 23.5, 24.5
  * worked great, front right still deg too fast
* aero 10 20
* default underfueled
* overtake green on corners 6 and 14
* speed green
* overcut

### Japan

* Lift @ 50 down 2, down 2 @ start of right red, coast in 5th, down 2 @ start of right red, 50, 1/2way, end of right red, in green, end of right red, 125
* Orange overtake on corners 1 and 10
* purple speed
* 27 27 24 24
  * Worked well.
    go long on hards
* preset 4
* aero 18 18
* trans 30/30
* leave geo as as

### bahrain

* 150, added road strip on left, street addon (must clip curb on left), left red plus plus, over the line as the left corner breaks, 90m, must clip curbs left right left, break at yellow sign, break short of under the sign
* Orange overtake at corners 1 and 4
* green speed
* preset 4, only tyres changed, diff 60 30
* 28.5 min 23.0 20.5
  * worked well

### Saudi

* Use speed5
* aero 0 0
* Dont go hards first
* suspension max min
* 25.5 26.5 21 20.5

### Miami

* blue, 50, road added, sign plus, red start, red start, sign
* Speed4
* aero 8 8
* 25,28.5,22,20.5
  * good

### Imola

* 100, corner clip down 4, 40, 40, dont clip inner corner but break right after, red, 80, as soon as shift to 4rd brake
* Speed 4
* aero 20 25
* diff 40 20
* suspension 40 10 21 1 25 40
* 23, 27.5, L, L

### Spain

* 100, 50, 50, halfway red, lift on line, 100, yellow on left, lift on line
* aero 36 30
* trans 50 30
* susp R L R 10 20 50
* Corners 1 and 10
* Orange overtake Orange speed
* 29.5, 26, 24,25
  * Worked well, esp hard
  * early pit didtn work
  * just use soft, med

### Canada

* white added, push aroundin 2nd, 75, 100, blue sign minus, black added, black sign plus
* 28.5, 27.5, 22.5.22
* speed 4 but front wing down to 8 and rear down to 12
* diff 60/50 for quali, 50/50 for race
* quali 1st, finished 7
* Start on mediums next time

### Austria

* aero 18/35 pinned down
* trans 60/35

### Silverstone

* lift in 7th, start of red, 3rd-2nd immediately, 50 down to 3rd, stay in 3rd till last inside red, 7th lift, down to 6th, down to 4th, 50 in 5th, start of red in 2nd
* throw into corners early
* overcut with hards
* aero 4/18
* trans 100/40
* suspension 36 18 21 1 25 50
* 29, 24, 24, 23.5

### Spa

* 125, red, 50, 50 lift and shift 2,
* aero 2/6
* trans 80/20
* susp 38 29 21 1 25 50
* tyres 24.5 25.5 23 23.5

### Hungary

* 100, 75, black on right, added grey, red minus, lift & downshift x3, red minus, black on right, on the line
* Go speed1 preset
* rear anti-roll 10
* 23.5, min, min, min
* good

### Zandvoordt

* 27, 22.5, 26, 24
* good

### Monza

* 29.5 29.5 23.5, 23.7
* Front wing 0
* Rear wing 2

* unknown if works since crashed into during race and quali

### Baku

* Same thing, crashes everywhere

### Singapore

* two stops good
* Max Max Low Low
* Balanced preset next time

### Texas

* R R 25.5 25.5
* Preset 2
* Hards are goatm softs last 5-6 laps

### Mexico

* R R L L
* aero 30,36
* suspension 38 29 12 6 25 50
* dont pit early

### Brazil

* 28 25 22 22
* Trim 3
* dont fuck with fuel levels

### Las Vegas

* R R L L

### Qatar

* R L R L
* Trim 1
* Aero 25 38
* both bars hard as can be

# Effects

### My starting setup

* Diff 50/30
  * Because apply full throttle while the car is still rotating, need to
    minimize the On-Throttle Differential.
    Setting between 50% and 55% allows rear wheels to rotate at significantly
    different speeds.
    prevents the inside wheel from losing grip and spinning the car when
    accelerate early.
* More negative camber (close to max negative)(slightly less negative on rears)
* both wings -3 on what they reccommend, with rear being equal or higher than
  front
  * require high-speed stability.
    should maximize the Rear Wing angle relative to the Front Wing.
    creates a "planted" rear end that can handle the load of early acceleration.
* Front wheel toe out 4 clicks
* rear toe 0
* suspension front max, rear min
* rear anti-rollbar min, front max
  * To resolve issues with curbs, maximize rear suspension compliance.
    Softening the Rear Springs and the Rear Anti-Roll Bar allows tires to stay
    in contact when hitting a curb, rather than bouncing and breaking traction.
* brake bias 60%
  * then soften front suspension if not stopping in time

* Tyres will degrade mainly because of two factors:
  * Rear tyre overheating
  * front tyre scrubbing from hard braking

* To find tyre pressure need to find how each is limiting
  * Start with 75% pressure in all tyres
  * Monitor tyre temp over 5 laps, looking to settle in ideal temp range
  * if too high on:
    * front surface or during braking:
      decrease psi
    * front inner or on fast areas:
      increase psi

### Tyres

| Compound | Ideal Temp |
|----------|------------|
| C1       | 105        |
| C2       | 95         |
| C3       | 90         |
| C4       | 85         |
| C5       | 80         |
| C6       | 75         |

### Pit loss table

Round Circuit Pit Loss (3s stop)

| Track                  | Time Lost |
|------------------------|-----------|
| Melbourne              | ~22.0     |
| Shanghai               | ~24.5     |
| Suzuka                 | ~22.0     |
| Bahrain (Sakhir)       | 23.7      |
| Jeddah                 | ~27.0     |
| Miami                  | ~26.0     |
| Imola                  | ~24.0     |
| Monaco                 | 19.9      |
| Barcelona              | ~22.5     |
| Montreal               | ~24.0     |
| Spielberg (Austria)    | ~21.0     |
| Silverstone            | 20.4      |
| Spa-Francorchamps      | ~24.5     |
| Hungaroring            | ~22.5     |
| Zandvoort              | ~21.0     |
| Monza                  | ~21.5     |
| Baku                   | ~26.5     |
| Singapore              | ~26.0     |
| COTA (Austin)          | ~23.0     |
| Mexico City            | ~23.5     |
| Interlagos             | ~21.0     |
| Las Vegas              | ~27.5     |
| Lusail (Qatar)         | ~27.0     |
| Yas Marina (Abu Dhabi) | ~23.5     |

### Car wont turn (understeer)

* inc fw, or dec rw

### Sliding/Spinning (oversteer)

* dec fw or inc rw
* tweak off-throttle diff

### Curbs ruin aero

* Softer suspension
* Higher ride height

### High speed snap

* More rear wing
* lower rear anti-roll

### Poor traction

* More rear wing
* higher rear ride height

### Poor rotation

* lower brake balance 5

### Wet

* Increase Grip by upping both wings +30
* Set both diffs to 50%
* Softer suspension to counter aquaplaning
* higher ride height
* Move brake bias forward

# References
