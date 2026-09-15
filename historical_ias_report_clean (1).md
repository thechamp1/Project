# FINAL PROGRESS REPORT ON THE PHYSICAL REALIZATION OF AN ELECTRONIC COMPUTING INSTRUMENT

**By:** Herman H. Goldstine, James H. Pomerene, Charles V. L. Smith
**Project Director:** John von Neumann
**Institution:** The Institute for Advanced Study, Electronic Computer Project
**Date:** January 1954
**Contracts:** W-36-034-ORD-7481 and DA-36-034-ORD-19 (Project No. TB3-0007 F)

---

## Page 1
Institute for Advanced Study
Math. • Nat. Sci. Library
Princeton, N. J. 08540

---

## Page 2
FINAL PROGRESS REPORT
ON THE PHYSICAL REALIZATION OF AN ELECTRONIC COMPUTING INSTRUMENT

by

Herman H. Goldstine
James H. Pomerene
Charles V. L. Smith

IAS ECP list of reports, 1946-57. no. 15.

THE INSTITUTE FOR ADVANCED STUDY
ELECTRONIC COMPUTER PROJECT
January 1954

---

## Page 3
PREFACE

This report has been prepared under the terms of Contracts W-36-034-ORD-7481 and DA-36-034-ORD-19 (Project No. TB3-0007 F) between the Research and Development Service, U. S. Army Ordnance Corps and the Institute for Advanced Study. It is a final report on the latter contract, covering the period up to 1 July 1952.

This report is issued in two parts: Part I (text) and Part II (drawings). Part II is separate from this volume and comprises the complete circuit drawings for the completed machine.

Certain accessory devices, notably a magnetic drum and an IBM input-output system, were added in the period subsequent to 1 July 1952. These will be described in a following report.

John von Neumann
Project Director
Institute for Advanced Study

---

## Page 4
TABLE OF CONTENTS

### Part I
* Preface
* Chassis List
* Drawings List
* Figures List
* I. Mathematical Aspects | 1
* II. The Orders | 22
    * 0.1 The Plus Clear Order | 22
    * 0.2 The Plus Hold Order | 23
    * 0.3 The Minus Clear Order | 24
    * 0.4 The Minus Hold Order | 24
    * 0.5 The Plus Absolute Clear Order | 25
    * 0.6 The Plus Absolute Hold Order | 25
    * 0.7 The Minus Absolute Clear Order | 26
    * 0.8 The Minus Absolute Hold Order | 26
    * 0.9 The Multiply No-Round Off Order | 27
    * 0.10 The Multiply Round Off Order | 28
    * 0.11 The Division Order | 28
    * 0.12 The Load RII Order | 29
    * 0.13 The Store Order | 30
    * 0.14 The Store Clear Order | 30
    * 0.15-0.16 The Unconditional Transfer Orders | 31
    * 0.17-0.18 The Conditional Transfer Orders | 32
    * 0.19 The Quick Sum Order | 33
    * 0.20 Right Shift, No Round Off Order | 34
    * 0.21 Right Shift, Round Off Order | 35
    * 0.22 Left Shift Order | 35
    * 0.23 The R₂ to R₃ Order | 36
    * 0.24-0.25 IBM and Drum Priming Order | 37
    * 0.26 IBM Input to Memory Order | 38
    * 0.27 IBM Output to Memory Order | 39
    * 0.28 Drum Input to Memory Order | 39
    * 0.29 Drum Output from Memory Order | 40
* The digital representation of orders. | 41

---

## Page 5
TABLE OF CONTENTS (continued)

* III. Circuit Elements | 42
* IV. The Arithmetic Organ | 49
    * The Registers | 49
    * Adder and the Digit Resolver | 62a
* V. The Williams Memory | 71
    * Williams Memory Block Diagram | 71
    * Memory Clock | 77
    * Williams Tube Pulsers | 81
    * The Williams Tube Output Amplifier | 87
    * The Discriminator | 87a
    * Pulse Routine Generator | 98
    * Williams Tube Deflection Generator | 100
    * Williams Memory Local Control | 105
* VI. The Control | 113
    * The Shift Counter | 113
    * Recognition Circuit | 122
    * The Address Dispatch Gates | 126
    * The Gate-Clear Sequencing Chain | 126
    * The Dispatch Counter | 138
    * The Main Control Organ | 144

### Part II
* Drawings

---

## Page 6
CHASSIS LIST

| Chassis Designation | Principal Function | See Drawing |
| :--- | :--- | :--- |
| A | Adder | B-1465 |
| Ā | Wms. Ā Pulser | A-1216 |
| B | Wms. B pulser | A-1216 |
| Ch₁₋₅ | Clear-Gate Chain | C-1449 |
| CL | Wms. CL Pulser | A-1216 |
| CLK | Wms. Clock | A-1217 |
| Com GS (or C G_m) | Complement Gate Selector | O-1458a |
| CT₀A | Disc. Toggle Clear --> 0 Driver | A-1459 |
| CT₁D | Disc. Toggle Clear --> 1 Driver | A-1459 |
| DC_t | Dispatch Counter | B-1471 |
| Del | Carry Delay timer | A-1459 |
| DR | Digit Resolver | B-1465 |
| HH | Wms. HH pulser | A-1216 |
| HT | Wms. HT pulser | A-1216 |
| LR | Left-Right selector | A-1451 |
| I | Wms. I pulser | A-1216 |
| M | Main Control | C-1422 |
| MD | Wms. address and "down" control for magnetic drum | --- |
| M/# | Number or magnitude gates | O-1458a |
| P₁₋₃ | Accept-Reject selection for division | O-1463 |
| QS | Control for Quick Sum | A-1469 |
| 2⁻¹R₁ | Extra RI stage for shifts | A-1446 |
| RI | Accumulator register | C-1322 |
| RII | Arithmetic register | C-1322 |
| RIII | Memory register | C-1323 |
| RII CS | R₂ clear selector | A-1453 |
| RII GD | RII Gate driver drivers | B-1456 |
| RI, II GS | RI and RII Gate selector | B-1456 |
| RII Op | Gates and clears for 2⁻³⁹ R₂ | A-1457 |
| R₂ to R₃ | Control of non-Wms. orders | A-1485 |
| RIII CGDD | Wms. to RIII gates and clears | A-1462 |
| RI CS | R₁ clear selector | A-1452 |
| RI GD | RI Gate driver drivers | B-1456 |

---

## Page 7
CHASSIS LIST (continued)

| Chassis Designation | Principal Function | See Drawing |
| :--- | :--- | :--- |
| BCR¹ | Clear R¹ to 0 driver | A-1459 |
| BCR² | Clear R² to 0 driver | A-1459 |
| BCR³ | Clear R³ to 0 driver | A-1459 |
| GrCR₁ | Clear R₁ to 1 driver | A-1459 |
| GrCR₂ | Clear R₂ to 1 driver | A-1459 |
| GrCR₃ | Clear R₃ to 1 driver | A-1459 |
| RCR¹ | Clear R¹ to 1 driver | A-1459 |
| RCR² | Clear R² to 1 driver | A-1459 |
| RCR³ | Clear R³ to 1 driver | A-1459 |
| SD | Wms. SD Pulser | A-1216 |
| SG A₁₋₂ | Wms. pulse routine generator | O-1470 |
| S_t C_t | Shift counter | C-1467 |
| TD | Wms. TD pulser | A-1216 |
| TH | Wms. TH pulser | A-1216 |
| TT | Wms. TT pulser | A-1216 |
| W | Williams control | C-1474 |
| YCR₁ | Clear R₁ to 0 driver | A-1459 |
| YCR₂ | Clear R₂ to 0 driver | A-1459 |
| YCR₃ | Clear R₃ to 0 driver | A-1459 |
| UnX | End correction for multiplication | A-1446 |
| X₁₋₂ | Multiplication control | B-1450 |
| 2⁰OB | --- | A-1447 |
| 2⁻³⁹RIII | --- | A-1485 |
| CylA | --- | B-1450 |
| CylB | --- | B-1465 |
| Wms. Amplifier | --- | A-1367 |
| Wms. Discriminator | --- | A-1241 |

---

## Page 8
DRAWINGS LIST

* C-3-1161 Memory High Voltage Supplies.
* C-3-1167 Memory High Voltage Meter Box.
* C-3-1168 Memory High Voltage Regulator.
* A-1216 Williams Tube Pulser.
* A-1217 Memory Clock.
* A-1241 Discriminator.
* B-1284 Deflection Input and Adder System.
* A-1285 Deflection Driver System.
* A-1288 Diode Bumper Strip for Digit Resolver Output.
* C-1289 Shift Counter.
* C-1322 Typical RII and RI Chassis Schematic.
* C-1323 Complement Gates and RIII Schematic.
* C-1334 Typical Adder Circuit.
* A-1367 Williams Amplifier.
* C-1422 Main Control.
* A-1426 Manual Control.
* A-1446 2⁻¹ RI Stage and Special X Chassis.
* A-1447 2⁰ End Outboard Chassis.
* C-1449 Gate-Clear Sequencing Chain.
* B-1450 Multiplication Terminate.
* A-1451 Left-Right Selector.
* A-1452 R₁ Clear Selector.
* A-1453 R₂ Clear Selector.
* A-1454 RI, RII End Around Circuits.
* A-1455 Carry Delay Unit.
* B-1456 RI, RII Gate Selector.
* A-1457 2⁻³⁹ R₂ Input, Clear, and Gates.
* O-1458a Complement Gate Selector and Magnitude/Number Ckt.
* A-1459 Typical Clear Driver Chassis.
* A-1462 RIII Gate and Clear Drivers.
* O-1463 Accept-Reject Selector.
* B-1465 Adder and Digit Resolver.
* B-1466 Instruction Synthesis - Main Control.
* C-1467 Shift Counter and Recognition Circuit.

---

## Page 9
DRAWINGS LIST (continued)

* A-1469 Quick Sum Control.
* O-1470 Routine Generator.
* B-1471 Dispatch Counter.
* A-1472 Williams Pulse Chain.
* A-1473 Discriminator Pulse Routines.
* C-1474 Williams Control.
* O-1477 Register Side of Machine.
* O-1478 Adder Side of Machine.
* B-1481 Williams Tube Assembly.
* A-1485 R₂ to R₃ Clear-Gate Chain and Artificial Sync.
* A-1486 Multiplication Variants.

---

## Page 10
FIGURES LIST

| Figure Number | Page Number | Figure Number | Page Number |
| :--- | :--- | :--- | :--- |
| I.1 | 6 | 19 | 86 |
| I.2 | 6 | 20 | 87a |
| I.3 | 12 | 21 | 89 |
| I.4 | 13 | 22 | 93 |
| I.5 | 14 | 23 | 95 |
| I.6 | 14 | 24 | 96 |
| | | 25 | 97 |
| 1 | 42 | 26 | 108 |
| 2 | 43 | 27 | 111 |
| 3 | 45 | 28 | 112 |
| 4 | 45 | 29 | 115 |
| 5 | 47 | 30 | 121 |
| 6 | 47 | | |
| 7 | 48 | I | 145 |
| 8 | 51 | II | 143 |
| 9 | 53 | III | 150 |
| 10 | 56 | IV | 151 |
| 11 | 57 | V | 153 |
| 12 | 59 | VI | 155 |
| 13 | 61 | VII | 158 |
| 14 | 70 | VIII | 160 |
| 15 | 71 | IX | 161 |
| 16 | 73 | X | 162 |
| 17 | 76 | XI | 163 |
| 18 | 78 | XII | 165 |

---

## Page 11
### I. MATHEMATICAL ASPECTS

In the succeeding pages of this chapter we shall describe the workings of the principal organs of the machine insofar as they concern the preparation of codes. We assume the reader is familiar with a previous report entitled, "Preliminary Discussion of the Logical Design of an Electronic Computing Instrument" (1946) by Burks, Goldstine, and von Neumann; in future references we indicate this report by FD. In this chapter we discuss those features of the arithmetic part of the machine which are relevant from a mathematical point of view.

In a consideration of the Arithmetic Organ one is naturally led first to discuss the number system employed. In spite of a long standing tradition in favor of the decimal system we were led both by logical and engineering considerations to employ the binary system. Since the control portions of the machine are carrying out purely logical functions and since logics are best expressed as binary operations the reasons for a binary representation, at least, of the orders for the machine are evident. On the engineering side the components out of which the machine is constructed are again binary in nature: The "flip-flop" is fundamentally a binary device; the "gate" is also; and the process of storing charge in the dielectric face or screen of the cathode ray tube used in the Memory is again of this same character. Hence, if one contemplates employing the decimal system, one is forced to a binary coding of the decimal system, each decimal digit being represented by a tetrad of binary digits. Thus a precision of 10 decimal digits would require 40 binary digits.

---

## Page 12
But in a true binary representation about 33 digits suffice to achieve a precision of $10^{10}$. Thus one is led to use Memory space -- recall that this is the most "expensive" portion of the instrument -- wastefully. It will also be seen as the discussion proceeds that the arithmetic portions of the machine are much simpler logically and hence engineering-wise in the binary system than in the decimal one.

To illustrate this latter point consider the problem of multiplication. In the binary system the product of a number $x$ by a binary digit is either $x$ or null according as the digit is 1 or 0. In the decimal system, on the other hand, there are ten possible values for the product of a digit by $x$: $0 \cdot x, 1 \cdot x, \dots, 9 \cdot x$. Thus decimal multiplication is fundamentally a more complex operation than is the binary one and this will be expressed in a decimal instrument either by a circuit complication or by the multiplication being slower. Similar remarks can be made about the other arithmetic processes.

It is often argued that notwithstanding these complications the decimal system is easier from the human point of view. Our machine, however, is such that data may be introduced either binarily or decimally and can be withdrawn in the same fashion if desired, and this without any circuitry. The conversions are trivially handled by extremely simple codes.

It is perhaps well to give at this point some details on the method of introducing data into the machine to enable the reader to develop gradually a feeling for the overall economy of our establishment. Each piece of information is introduced as an aggregate of 10 quantities in the hexadecimal system.

---

## Page 13
In this number system there are 15 integers $\bar{0}, \dots, \bar{9}, \overline{10}, \overline{11}, \overline{12}, \overline{13}, \overline{14}, \overline{15}$ which we call $0, \dots, 9, A, B, C, D, E, F$. Thus the first 10 of these integers are exactly the decimal integers, so that a decimal quantity introduced into the machine is given its familiar and usual form. A binary number or order — these are in binary form as will be explained in the chapter on the code — is expressed as 10 tetrads of binary digits, i.e., as 10 hexadecimal integers.

The decision as to whether a given quantity is to be treated by the machine as the decimal representation of a given number or as the hexadecimal representation of a binary number is left to the coder. I.e., he knows which of the data he has introduced is decimal and must be converted by the machine into a binary form and which is already binary. This decision places no more burden on the coder than does that one which requires him to know which data are orders and which are numbers. Indeed, the two problems are quite intimately related. Generally, in coding a given problem it is the practice to place in a block of consecutive positions the decimal information. This makes the conversion of these numbers into their binary form a simple inductive procedure determined only by the number of places desired and the locations of the initial and terminal quantities.

We leave this subject for the present and return to it later after we have described the orders themselves.

The Arithmetic Organ is a 40-fold aggregate of binary units. We use the first of these to record the sign digit of a number and the remaining 39 for digital information. Thus each "word", i.e., aggregate of 40 binary digits, viewed as a binary number has a precision of $2^{-39} \sim 10^{-11.7}$.

---

## Page 14
We have chosen to fix our binary point immediately to the left of the first digit of numerical material, i.e., the binary point is fixed immediately after the sign digit. Thus the digits — apart from the sign — have positional values $2^{-1}, 2^{-2}, \dots, 2^{-39}$. As a matter of fact, as far as our Adder is concerned the sign is treated as a binary digit with positional value $2^0$.

Before proceeding from this point it is well to discuss our treatment of negative numbers in the machine since this has bearing on the character of the Arithmetic Organ. To do this we say first a word about our Adder. If one regards our numbers $x = (x_0, x_1, \dots, x_{39})$ as 40-digit quantities $x_0 \cdot 2^0 + x_1 \cdot 2^{-1} + \dots + x_{39} \cdot 2^{-39}$, then our Adder as far as digit-adding and carrying mechanisms are concerned functions identically in all places with one exception: If a carry proceeds from the left-most digit, it is "lost" (cf., however, our discussion below of the division operation). This means clearly that the augend and addend, both of which lie between 0 and 2 have produced a sum greater than 2 will omit the 2. This is, of course, nothing other than a statement that the Adder functions modulo 2.

In this sense all numbers represented in the machine can be viewed as being modulo 2. We have used this fact to determine our representation of negative numbers. If $x$ is an arbitrary real number, then there is exactly one number $\bar{x}$ between 0 and 2 with which it agrees modulo 2, i.e., for each $x$ there is a unique $\bar{x}$ such that $0 \le \bar{x} < 2$ and $x \equiv \bar{x} \pmod 2$. This fact fixes our representation of negative numbers.

---

## Page 15
We agree always to deal with numbers $x$ for which $-1 \le x < 1$. Now the $\bar{x}$ associated with $x$ is $x$ if $x \ge 0$; thus, $0 \le \bar{x} < 1$ in this case we represent $x$ by the digitalized form of $\bar{x}$. It clearly has $x_0$, its sign digit +, i.e., 0. If $x < 0$, then $\bar{x} = x + 2$ and we have $1 \le \bar{x} < 2$, i.e., the left-most digit of $\bar{x}$ is 1, i.e., -. Thus we always represent a number $x$ by the digitalized form of $\bar{x}$ and have the convention that + is 0 and - is 1 with the left-most digit being the sign.

In closing this discussion we mention the relation of our representation of negative numbers with that of "complementation". Consider a negative number $x$ with $-1 \le x < 0$ and let $y = -x$. Then $0 < y \le 1$. As we said above we digitalize $x$ by representing it as $x + 2 = 2 - y = 1 + (1 - y)$. Then the left-most digit of this representation is, correctly, 1 and the remaining digits are those of the complement of $y = |x|$. This is what is frequently called the representation by complementation of negative numbers.

The Arithmetic Organ proper contains the following principal units: 3 Registers of 40 digits each (cf. however, below for an exception to this), an Adder, various sets of gates whose functions will be made clear in what follows, and a Control Unit to supervise the performance of the various Arithmetic orders. In the accompanying figure we show schematically the interrelations between some of these and in later figures we show more details.
