# Final Progress Report on the Physical Realization of an Electronic Computing Instrument

**Herman H. Goldstine, James H. Pomerene, Charles V. L. Smith**

IAS Electronic Computer Project — January 1954

IAS ECP list of reports, 1946–57, no. 15


---


> **Note on this transcription.** This Markdown edition was produced from a scanned copy
> (via the Internet Archive) run through OCR. The OCR text is used as the backbone; pages
> where the OCR failed outright or was too garbled to trust have been retranscribed by hand
> against the page images, and all diagrams, circuit schematics, and photographic plates are
> embedded below as images (see the `images/` folder) rather than transcribed, since ASCII
> reproduction of circuit drawings is not reliable. Minor OCR artifacts (scanno noise such as
> misread digits, stray punctuation) may remain in body text on pages that were not otherwise
> flagged, but the OCR is generally faithful there. Figure/page cross-references below use the
> physical PDF page number, not the printed page number in the original document.


---

## Front Matter

Institute for Advanced Study
Math. & Nat. Sci. Library
Princeton, N. J. 08540

---

FINAL PROGRESS REPORT
ON THE PHYSICAL REALIZATION OF AN ELECTRONIC COMPUTING INSTRUMENT

by

Herman H. Goldstine
James H. Pomerene
Charles V. L. Smith

IAS ECP list of reports, 1946-57, no. 15.

THE INSTITUTE FOR ADVANCED STUDY
ELECTRONIC COMPUTER PROJECT
January 1954

---

This report has been prepared under the terms of Contracts
W-36-034-ORD-7481 and DA-36-034-ORD-19 (Project No. TB3-0007 E)
between the Research and Development Service, U. S. Army Ordnance
Corps and the Institute for Advanced Study. It is a final report on
the latter contract, covering the period up to 1 July 1952.

This report is issued in two parts: Part I (text) and Part
II (drawings). Part II is separate from this volume and comprises
the complete circuit drawings for the completed machine.

Certain accessory devices, notably a magnetic drum and an IBM
input-output system, were added in the period subsequent to 1 July
1952. These will be described in a following report.

John von Neumann
Project Director
Institute for Advanced Study


---

## Chassis List


| Chassis Designation | Principal Function | See Drawing |
|---|---|---|
| A | Adder | B-1465 |
| Ā | Wms. Ā Pulser | A-1216 |
| B | Wms. B pulser | A-1216 |
| Ch 1-5 | Clear-Gate Chain | C-1449 |
| CL | Wms. CL Pulser | A-1216 |
| CLK | Wms. Clock | A-1217 |
| Com GS (or CmGs) | Complement Gate Selector | O-1458a |
| CT1A | Disc. Toggle Clear → 0 Driver | A-1459 |
| CT1D | Disc. Toggle Clear → 1 Driver | A-1459 |
| DCt | Dispatch Counter | B-1471 |
| Del | Carry Delay timer | A-1455 |
| DR | Digit Resolver | B-1465 |
| HH | Wms. HH pulser | A-1216 |
| HT | Wms. HT pulser | A-1216 |
| LR | Left-Right selector | A-1451 |
| I | Wms. I pulser | A-1216 |
| M | Main Control | C-1422 |
| MD | Wms. address and "down" control for magnetic drum | — |
| M/# | Number or magnitude gates | O-1458a |
| P1-3 | Accept-Reject selection for division | O-1463 |
| QS | Control for Quick Sum | A-1469 |
| 2¹R¹ | Extra RI stage for shifts | A-1446 |
| RI | Accumulator register | C-1322 |
| RII | Arithmetic register | C-1322 |
| RIII | Memory register | C-1323 |
| RII CS | R2 clear selector | A-1453 |
| RII GD | RII Gate driver drivers | B-1456 |
| RI, II GS | RI and RII Gate selector | B-1456 |
| RII Op | Gates and clears for 2⁻³⁹ R2 | A-1457 |
| R2 to R3 | Control of non-Wms. orders | A-1485 |
| RIII CGDD | Wms. to RIII gates and clears | A-1462 |
| RI CS | R1 clear selector | A-1452 |
| RI GD | RI Gate driver drivers | B-1456 |
| BCR¹ | Clear R¹ to 0 driver | A-1459 |
| BCR² | Clear R² to 0 driver | A-1459 |
| BCR³ | Clear R³ to 0 driver | A-1459 |
| GrCR1 | Clear R1 to 1 driver | A-1459 |
| GrCR2 | Clear R2 to 1 driver | A-1459 |
| GrCR3 | Clear R3 to 1 driver | A-1459 |
| RCR1 | Clear R1 to 1 driver | A-1459 |
| RCR2 | Clear R2 to 1 driver | A-1459 |
| RCR3 | Clear R3 to 1 driver | A-1459 |
| SD | Wms. SD Pulser | A-1216 |
| SO A1-2 | Wms. pulse routine generator | O-1470 |
| St Ct | Shift counter | C-1467 |
| TD | Wms. TD pulser | A-1216 |
| TH | Wms. TH pulser | A-1216 |
| TT | Wms. TT pulser | A-1216 |
| W | Williams control | C-1474 |
| YCR1 | Clear R1 to 0 driver | A-1459 |
| YCR2 | Clear R2 to 0 driver | A-1459 |
| YCR3 | Clear R3 to 0 driver | A-1459 |
| UnX | End correction for multiplication | A-1446 |
| X1-2 | Multiplication control | B-1450 |
| 2⁰OB | — | A-1447 |
| 2⁻³⁹RIII 0 | — | A-1485 |
| CyIA | — | B-1450 |
| CyIB | — | B-1465 |
| Wms. Amplifier | — | A-1367 |
| Wms. Discriminator | — | A-1241 |


---

## Drawings List


| Drawing No. | Title |
|---|---|
| C-3-1161 | Memory High Voltage Supplies |
| C-3-1167 | Memory High Voltage Meter Box |
| C-3-1168 | Memory High Voltage Regulator |
| A-1216 | Williams Tube Pulser |
| A-1217 | Memory Clock |
| A-1241 | Discriminator |
| B-1284 | Deflection Input and Adder System |
| A-1295 | Deflection Driver System |
| A-1288 | Diode Bumper Strip for Digit Resolver Output |
| C-1289 | Shift Counter |
| C-1322 | Typical RII and RI Chassis Schematic |
| C-1323 | Complement Gates and RIII Schematic |
| C-1334 | Typical Adder Circuit |
| A-1367 | Williams Amplifier |
| C-1422 | Main Control |
| A-1426 | Manual Control |
| A-1446 | 2¹ RI Stage and Special X Chassis |
| A-1447 | 2⁰ End Outboard Chassis |
| C-1449 | Gate-Clear Sequencing Chain |
| B-1450 | Multiplication Terminate |
| A-1451 | Left-Right Selector |
| A-1452 | R1 Clear Selector |
| A-1453 | R2 Clear Selector |
| A-1454 | RI, RII End Around Circuits |
| A-1455 | Carry Delay Unit |
| B-1456 | RI, RII Gate Selector |
| A-1457 | 2⁻³⁹ R2 Input, Clear, and Gates |
| O-1458a | Complement Gate Selector and Magnitude/Number Ckt. |
| A-1459 | Typical Clear Driver Chassis |
| A-1462 | RIII Gate and Clear Drivers |
| O-1463 | Accept-Reject Selector |
| B-1465 | Adder and Digit Resolver |
| B-1466 | Instruction Synthesis – Main Control |
| C-1467 | Shift Counter and Recognition Circuit |
| A-1469 | Quick Sum Control |
| O-1470 | Routine Generator |
| B-1471 | Dispatch Counter |
| A-1472 | Williams Pulse Chain |
| A-1473 | Discriminator Pulse Routines |
| C-1474 | Williams Control |
| O-1477 | Register Side of Machine |
| O-1478 | Adder Side of Machine |
| B-1481 | Williams Tube Assembly |
| A-1485 | R2 to R3 Clear-Gate Chain and Artificial Sync |
| A-1486 | Multiplication Variants |


---

## Figures List

*(Figure number → printed page number, as given in the original Figures List. Note: physical PDF page numbers used elsewhere in this document differ — see each figure's caption.)*


| Figure | Page | | Figure | Page |
|---|---|---|---|---|
| I.1 | 6 | | 19 | 86 |
| I.2 | 6 | | 20 | 87a |
| I.3 | 12 | | 21 | 89 |
| I.4 | 13 | | 22 | 93 |
| I.5 | 14 | | 23 | 95 |
| I.6 | 14 | | 24 | 96 |
| 1 | 42 | | 25 | 97 |
| 2 | 43 | | 26 | 108 |
| 3 | 45 | | 27 | 111 |
| 4 | 45 | | 28 | 112 |
| 5 | 47 | | 29 | 115 |
| 6 | 47 | | 30 | 121 |
| 7 | 48 | | I | 145 |
| 8 | 51 | | II | 148 |
| 9 | 53 | | III | 150 |
| 10 | 56 | | IV | 151 |
| 11 | 57 | | V | 153 |
| 12 | 59 | | VI | 155 |
| 13 | 61 | | VII | 158 |
| 14 | 70 | | VIII | 160 |
| 15 | 71 | | IX | 161 |
| 16 | 73 | | X | 162 |
| 17 | 76 | | XI | 163 |
| 18 | 78 | | XII | 165 |


---

## Part I — Text


<!-- p. 11 -->
I.
I. HATHEMATICAL A8FICTS
In the succeeding pages of this chapter ve shall describe the
workings of the principal organs of the nachlna Insofar as they con-
cern the preparation of codes. We eussuas the reader Is familiar with
a previous report entitled, "Preliminary Discussion of the Logical De-
sign of an Xlectronlc Computing Instrument" (19^) by Burks Ooldstlne,
,
and von Neumann; in future references ve indicate this report by FD.
In this chapter ve discuss those features of the arithmetic part of
the machine vhich are relevant from a mathematical point of vlev.
In a consideration of the Arithmetic Organ one is naturally led
first to discuss the number system employed. In spite of a long stand-
ing tradition in favor of the decimal system ve vere led both by logical
and engineering considerations to employ the binary system. Since the
control portions of the machine are carrying out purely logical func-
tions and since logics are best expressed aa binary operations the
reasons for a binary representation, at least, of the orders for the ma-
chine are evident. On the engineering side the components out of vhich
the HBchine Is constructed are again binary In nature: The "flip-flop"
is fundamentally a binary device; the "gate" is also; and the process of
storing charge in the dielectric face or screen of the cathode ray tube
used in the Hsmory is again of this same character. Hence, if one con-
templates employing the decimal system, one is forced to a binary coding
of the decimal system, each decimal digit being represented by a tetrad
of binary digits. Thus a precision of 10 decimal digits vould require

<!-- p. 12 -->
2.
kO binary digits. But In a true binary repreaentation about 33 dlgite
suffice to achleye a precision of 10 Thus one is led to use l^mory
—
space recall that this is the moat "expensive" portion of the Inatru-
mant -- vastefully. It will also be seen as the dlacueslon proceeds
that the arithmetic portions of the machine cure much simpler logically
and hence engineering-vise in the binary system than in the decimal one.
To Illustrate this latter point consider the problem of multipli-
cation. In the binary system the product of a number x by a binary digit
is either x or null according as the digit is 1 or 0. In the decimal
system,on the other hand^ there are ten possible values for the product
of a digit by x, 0.x, 1.x, ..., 9>x- Thus decimal nultiplication is
fundamentally a more complex operation than is the binary one and this
will be expressed in a decimal instrument either by a circuit complica-
tion or by the multiplication being slower. Similar remarks can be made
about the other arlthmatic processes.
It is often argued that not withstanding these complications the
decimal system is easier from the human point of view. Our machine,
however, is such that data may be introduced either blnarily or decimally
aind can be withdrawn in the same fashion if desired, and this without any
circuitry. The conversions are trivially handled by extremely simple
codes.
It is perhaps well to give at this point some details on the method
of Introducing data into the machine to enable the reader to develop
gradually a feeling for the overall economy of our establishiaent. Bach
piece of Infornation la Introduced as an aggregate of 10 quantities in

<!-- p. 13 -->
the hexadecimal syatem. In thia number syBtem there axe 15 Integers 0,
...,'§, To, TL, 12, 15, If, T5 which we call 0, ..., 9, A, B, C, D, i,
F. Thua the first 10 of these integers are exactly the decimal integers,
so that a decimal quantity introduced into the machine la given ita
famlliflLT and usual form. A binary nximber or order -- these are in binary
form as will be explained in the chapter on the code --is expressed as
10 tetrads of binary digits. I.e. as 10 hexadecimal integers.
The decision ais to whether a given quantity is to be treated by
the machine as the decimal representation of a given number or as the
hexadecimal representation of a binary number is left to the coder. I.e.,
he knows which of the data he has introduced is decimal and must be con-
verted by the machine into a binary form and which is already binary.
This decision places no more burden on the coder than does that one
which requires him to know which data are orders and which aire numbers.
Indeed, the two problems are quite intimately related. Generally, in
coding a given problem it is the practice to place in a block of consecu-
tive ixssitions the decimal information. This makes the conversion of
these numbers into their binary form a simple inductive procedure deter-
mined only by the number of places desired and the locations of the
initial and terminal quantities.
We leave this subject for the present and return to it later after
we have described the orders themselves.
The Arithmetic Organ is a kO-tolA aggregate of binary unlta. We
use the first of these to record the sign digit of a number and the re-
maining 39 for digital information. Thus each "word", i.e. aggregate of

<!-- p. 14 -->
.
If.
ko binary digits, viewed as a binary aumber has a precision of 2^^
-11.7.We
*. 10 have chosen to fix our binary point innisdiately to the
left of the first digit of numerical material, 1-e. the Jjlnary point
is fixed immediately after the sign digit. Thus the digits -- apart
from the sign -- have positional values 2. -1,2-2 , ..., 2 -'^Q . As a nat-
ter of fact, as far as our Adder is concerned the sign ia treated as a
binary digit with poeitional value 2
.
Before proceeding from this point it is well to discuss our
treatment of negative numbers in the machine since this has bearing on
the character of the Arithmetic Organ. To do this w© say first a word
about our Adder. If one regards our nunibers x = (x , x, , •.., x_q) as
-1 -'^9
lK)-digit quantities x • 2 + x • 2 + ... + x • 2 -^^ , then our
Adder as far as digit-adding and carrying mechaniaos are concerned
functions identically in all places with on* exception: If a carry
proceeds from the left-most digit, it is "lost" (cf., however, our dis-
cussion below of the division operation) This means clearly that the
.
augend and addend, both of which lie between and 2 have produced a
sum greater than 2 will omit the 2. This is, of course, nothing other
than a statement that the Adder functions modulo 2.
In this sense all nuabera represented in the machine cein be viewed
as being modulo 2. We have used this fact to determine our representa-
tion of negative numbers. If x is an arbitrary real number, then there
is exactly one number x between and 2 with which it agrees modulo 2,
i.e. for each x there is a unique x such that < i < 2 and x - x (mod 2)
This fact fixes our representation of negative nunibers.

<!-- p. 15 -->
5.
We ajjree alweys to '.oal wttb n.-mtors x for which -1 < jj < 1.
Now the X associated vlth x la a If .t > 0; thus, < 7 < 1 in this
case we represent x by the dljltallzed form of 7. It clearly haa
Xq, Its sign digit +, I.e. 0. If x < 0, then x » x + 2 and va have
1 < X < 2, I.e. the loft-most dlglli of x is 1, i.e. -. Thua we always
represent a number x by the dlgltallzed form of x and have the conven-
tion that + is and - is 1 with the left-moat digit being the sign.
In cloalng thia discussion we motition the relation of our repre-
sentation of negative numbers with that of "oompleiasntatlon'' Consider
.
a ne^tlve number i with -1 < x < and let y « -x. Then < y < 1.
As we said above ve digltalize x by representing itasx+2=2-y=
1 + (1 - y)- Then the left-most digit of this representation la,cor-
rectly, 1 and the remaining digits are those of the complement oT j =*
I X j . This is what is frequently called the representation by comple-
mentation of negative numbers.
The Arithmetic Organ proper contains the following principal
units: 3 Eegisters of 14^0 digits each (cf. however, below for an excep-
tion to thia), an Adder, various sets of gates whose functions will be
made clear in what follows, and a Control Onit to supervise the perform-
ance of the various Arithmetic orders. In the accompanying figure
we show schematically the interrelations between some of these and in
later figures we show more details.

<!-- p. 16 -->

![Fig. I.1 — Register I/II/III and Adder](images/fig_I1.jpg)
*Fig. I.1 — Register I/II/III and Adder*


![Fig. I.2 — Complement Gates between RIII and the Adder](images/fig_I2.jpg)
*Fig. I.2 — Complement Gates between RIII and the Adder*

6.
Rfitjistcr I
^ Arid^Pf^
ge.gt'^-t-er HI
Pig. I. 1.
As Indicated in the figure the inputs (UO-fold in each case) to the Adder
—
are from Begisters I and III we shall use the suobols BI and Bill in
the future -- and the output of this unit is stored back in BI. Again
InforiBatloQ in Bill can be conanunlcated to BII and hence to BI without
proceeding through the Adder. In an addition the augend is originally
in BI and the addend in Bill, the sum being placed in BI at the comple-
tion of the operation.
To make clear the subtraction we must make mention of a unit
called the Complement Gate Chaasie which intervenes between Bill and
the Adder, as indicated in the figure below.
Comp(enien+ CcirrccVi'oi

<!-- p. 17 -->
7.
This chaaslB permits one of three modea of co««uiilcatlon between
Bill and the Adder. If a number x la stored in RIII, then either the
Complement Gates permit x, the complement of x or to enter the Adder;
or, to bo more precise, If x « (x^, x^ ..., x -) , then either x or
(1 = ^Q> l-»]^» •'-, 1-^30) or » (0, 0, ..., 0) is permitted to enter
the Adder from RIII. If it is the middle case, then the Arithaetlc
Control also "Injects" a digit 2 into the Adder. This, aa ve shall
see, correctly handles the operation of subtraction.
To form x - y ve proceed as follows: the ArithiMtic Organ haa
X in BI, y in Bill and haa been instructed to form the difference. It
f#rmB, apart from the "compleAsnt correction" Just mentioned,
ZIj^ (x^ + (1 - y^)) • 2"^ = x + (2 - y) - 2"^^. The complement
-39
correction then has the effect of removing this last 2 and yielding
the correct difference.
Ve leave this diacusaion of the separate iinlts of the Arithmetic
Organ for the moment but with the intention of returning to it shortly.
The multlplioation operation is somewhat more delicate in a cer-
tain sense than are the addition and subtraction because the procedure
based on the modulo 2 fails completely. If one changes one.factor, say
X, of a product xy by a two, then the new product differs from xy by 2y
which is not generally an Integer multiple of 2 since -1 < y < +1.
To effect a multiplication we store the multiplication in BII
and the multiplicand in RIII. We carry out the process by seriatim
multiplying the entire multiplicand by the digits of the multiplier
starting with the least significant one.

<!-- p. 18 -->
8.
The multiplication proper takes place In 39 steps, corresponding
to the 39 non-8Ign digits of the multiplier, together with several "clean-
up" operations In addition. We describe all this below. For simplicity
we first consider the case in which both the multiplier x ^ (x , x.,, ...,
x^^) and the multiplicand y - (y^, y^^, ..., y^^), I.e. x^ - y^ - and
0<x>l, 0<y<l.
hence
1-1
Aaaume we have already performed the first steps of the
multiplication involving the multiplication of the multiplicand by the
1-1
last digits of the mtultiplier, x-_, i-g, ..., x.^ .. We describe
now the multiplication with the i-th digit, i.e. with 3tj^_.. Assume
that HI contains the partial product after the last step, V^_-^ (for
i = 1, p- = 0). We form
f f°^ ^o-i = °
2p. - P. , + y^ vith y =
^
I.e. if Xj^ we define p^ as l/2 of •p^_^ and if ^i^_^ =» 1 as 1/2
of (p^ -, + y) • Consider now the sizes of the (luantitles 2p.. For i « 0,
< 2p. < 2 (since p =0); now If this ia true for i - 1, then our dis-
played definition above makes it also true for 1. Thus 2p^ lies in the
interval < 2p < 2 and no carry can arise beyond 2 -position.
Thus p. is formed from 2p by a right shift with the sign digit
Bade 0. Finally we have
p^^ = 2"^(2"^(2"^(...(2"^ x^^ y + X38 y)---)* Xj^ y =
i.e. we have our correct product. We describe Later how we achieve this
in the Arithmetic Organ. At the moment, however, we turn Instead to the

<!-- p. 19 -->
9.
other possible caneg namely: i<0, y>0, x<0, y<0, x>0 y<0.
.
We pass new to these cases and describe hov they are performed.
If X < 0, then It is represented in the machine aa x + 2. Thus for x < 0,
y > the procedure we have Just described would form not xy but xy + 2y;
for X < 0, y < it would form xy + 2x + 2y + 1*; for x > 0, y < it would
form xy + 2x. Hence, correction terms 2x, 2y or both would be needed. As
we shall see later these corrections would be quite awkward for us to per-
form, particularly the correction 2x tlnce we in fact lose the digits of
the multiplier as they eure no longer needed. The reason for this will
become apparent in the next section.
Otir procedure is this: First let us assume that the corrections
necessitated by y < have been disposed of and permit y to be either <
or > 0. We focus attention now on x < 0.
We disregard the sign digit of x and act as if it were 0. Then x is
replaced by x - x - 1 but since -1 < x<Ox will act as if it were (x - 1)
+ 2. Hence our procedure for multiplication will produce x y - (x + 1) y =
xy + y. We therefore need a final correction in this case of -y at the
end of the process. Thus in the cases x < we proceed throu^ the 39
steps described earlier and thereby form xy + y and then we must perform
another step to subtract out the multiplicand y.
Having disposed of the difficulties that arise when x < 0. we may
now assume x > and consider the one remaining case, »»Bely y < 0.
Suppose this time that we Ignore completely the sign digit of y,
or rather that we replace it by 0. Then if y = y - 1, we have a« before
xy = x(y +1) = xy + X and a correction -x is needed. Since, however,

<!-- p. 20 -->
:
10.
we do not have x, the multiplier, available at the end of the multiplica-
tion we must find a means of applying this correction as tlie first 39
steps proceed.
We proceed in this fashion: when we examine th« digit x^q of
the multiplier, we normally add into the partial product p. the number
y if x-,_ . = 1 and otherwise. Let us now modify this procedure as
follows
ri for x^ -
^
*"^
2Pl = Pi-1 * ^1 ^i - ^ 1
L^ '°' 'lK)-i " ^-
As before < 2p. < 2 and no carries can proceed beyond the 2 -
position. Let us see now what result we have produced by this procedure.
P39 = 2" (2' (£" (...(£" x^^y + 2' (I-3C39) + x^gy + (l-x^g))...) +
+ Xgy + (l-Xg)) + x^y + (1-x^) =»
2».,
= x(y+l) + 1 - 2'^^ - X = xy + (1 - 2'^^).
-39 '
Thus a final correction of -1 + 2 is necessary. But this correction
which is done at the end can be effected modulo 2 and we can correct it
by 1 + 2'^^.
We summarize now in a general deecriptlon covering all four cases.
We return now to our schematic discussion of the Arithawtic Organ.
Since we wish to retain the full 78 digits of a product, we have estab-
lished certain interconnections between BI and HII not yet shown In
Figure I.l. Before describing them we must indicate another feature of
RI and PII. Each of them Is capable not only of receiving Uo digit

<!-- p. 21 -->
11.
numbers and of tranaiiiittiin,4 them, hm also of trunalating either to the
right or left whatever information le stored in them. We dlscufla tho
logical implicationa of these shift facilities later. At the moment ve
prefer to indicate how this is accomplished, at Least in a crude way.
Each of EI and RII is in redity not one but two registers suit-
ably interconnected. Let us consider Rl first. It consists of two
registers and four sets of ^-fold gates. Let the two registers be
denoted by B and R . One set of gates intervenes between the Adder
and R Thus the output of the Adder is stored at least initially in
.
H . Two seta of gates allow coraraunlcation from B to B^ and a fourth
set allows communication from R to R
.
The set which controls the communication between the Adder and
R the so-called Green Gates, is so wired that it makes digital posi-
,
tion 2" of the Adder correspond to 2~ of B . One of the two sets con-
T
trolling the route from B"^ to R^, the so-called Red Oetes, raakea posi-
tion 2" of R correspond to 2" " of tti; the other sot, the ao-called
Black Gate, raakea 2'^ of R""" correspond to 2"^^^^ of R . The fourth
set, the so-called Yellow Gate, from Rj. to B nakea 2'*" of B correspond
to 2' of B We indicate thla below In TlgiJre T.3.
.
A similar arrangement obtains with respect to BII. The structure
of RIII la, however, simpler since It Is not called upon to perform
shifting functions as are BI and BII.

<!-- p. 22 -->

![Figure I.3 — Gate sets (Red/Black/Green/Yellow) between RI and RII](images/fig_I3.jpg)
*Figure I.3 — Gate sets (Red/Black/Green/Yellow) between RI and RII*

12.
Prri^TCi+C
Ye lowGc»tc
I
L_ii'Z] L+l
Figure I.3.
We can now describe in somewhat more detail the operations
previously olluded to such as the ri^t and left ahifte, the transfer
into "RI, the addition, the subtraction, and at least part of the multi-
plication.
Consider first a nuaber in E^ -- in both RI and BII the units B
,
E serve only a3 transient storage positions; all storage for more
than a few aiicroaeconds io in B , E ^ -- which we desire to shift right
(left) . The Arithmetio Control routes the Information first to B via
the Yellow Gate set, thaiback to B^ via tha Black (Bed) Gate set. (We
must describe later treatment of the sign digit.)
Next consider a number arriving in KI from the Adder. It is
transferred to B via the Green Gate set, thenId B via the Bed set --
note this apparently causes the information in 2 -position of the Adder

<!-- p. 23 -->

![Figure I.4 — Connections between RI and the Adder](images/fig_I4.jpg)
*Figure I.4 — Connections between RI and the Adder*

13.
to be lost. Actually It does not becuaae RI haa a 2 poaitioa for
preclaoly thia reaaon; It is then aant back to E^ via the Yellow act
and finally back to R^. via the Black aet. Not* that it is now cor-
rectly positioned. I.e. the content of 2" -pcaitlon of H_ la that of
2~ -position of tha Adder.
In the next figure we indicate the connectiona between BI and
the Adder, suppreaaing the gate seta.
r

<!-- p. 24 -->

![Figure I.5 — Right-shift connection, RI to RII](images/fig_I5.jpg)
*Figure I.5 — Right-shift connection, RI to RII*


![Figure I.6 — Left-shift connection, RI to RII](images/fig_I6.jpg)
*Figure I.6 — Left-shift connection, RI to RII*

lU.
from RI to RII but not back again. This connection 1b provided so
that whenever a rl^t shift occurs the digits being shifted out of BI
are stored In RII. We make this connection quite specific In figure
I
1.5 below.
C I
RE
-c
Tlgure 1.5.
To provide for the comparable situation when a left shift occurs the
2'^
2° stage of-RI is connected to the stage of RII, as in Figure 1.6
belew.
RI
> _j BE
Figure 1.6.
We are now able to proceed further with the details of the
fflultlpllcatlon. The multiplier is initially placed in RII. (This
must be dona prior to the multiplication order, c.f. 0.9 below.) Then
when the multiplication is initiated the multiplicand is in R . An
observation post exists at stage 39 of RII which examinee whether the
digit therein is or 1 and acts accordingly, i.e. it does not or does

<!-- p. 25 -->
15-
add the multiplicand Into RI in case both multiplier and multiplicand
are positive. We diacuea below the exact detalla in all cases. Then
a right shift of one is performed. Thus three things occur of relevance:
first, the partial product in RI is properly positioned for the next step;
second, the digit of the oultiplier last examined has been loet and the
next relevant, i.e. the now currently relevant, is available at the
insx)ectlon station; third, the least signifioant digit of the partial
product has now been shifted into RII, into the leading sta^. This pro-
cedure is carried on for the 39 steps required at which time the 39 most
significant digits of the product appear in RI and the 39 least signifi-
cant ones in RII.
The addition oi>eratlon is performad in this fashion: We assume
the augend is now in RI, specifically in R_, and the addend is in R
The Complement Qates are set to pass the addend out and the sum is then
stored temporarily in R . This sum is then put into R displaced one to
the left with the sign digit in 2* . Next, the number is transferred
back to R and thenoe down to R- in the correct position. In terns of
the various gating operations this means the follovlng: The Oreen Gates
were opened to admit the sum to R the Red Gates sent it to R^; the
j
Yellow Gates sent it back to R ; and finally it arrived correctly posi-
tioned in R^ via the Black Gates.
The situation for the subtraction differs in one point only; the
Complement Gates are opened to pass the complement of the addend and
the complement correction is carried out.
In both cases the sign of the sum is now both in 2 and 2 .

<!-- p. 26 -->
•
16.
The possible addition and subtraction operationa performable by
the machine are these:
1. The addition (subtraction) of the contents of ' R TTT and of R
.
2. The addition (subtraction) of the contents of R'^'^^ and of R
pre-cleared to 0. I.e. the transfer of a number (or its compleosnt)
into R
.
3. The addition (subtraction) of the absolute value of the con-
tent! of R and of R-.
k. The addition (subtraction) of the absolute value of the con-
tents of B and of R- pre-cleared to 0. I.e. the transfer of the modu-
lus of a number (or its CTomplement) into R-.
To perform the -operations involving absolute values the Arlthaetic
Control is provided with a monitor vhich decides whether the Complement
Gates are to pass the number in R or its complement according as the
instruction requires.
The left shift is performed analogously to that for the rig^t shift
but the right-most stage of R^. is made 0.
This is the correct convention to ensure that the left shift is
exactly a multiplication by 2 (provided that the result is still in
"scale", i.e. is not outside the Interval -1 < x < 1)
The left shift operation can be performed n times (1 < n < U7) by
means of a single order.
The right shift operation is performed in this fashion: The num-
ber in R is transferred into R I and is then sen ' t back Into H displaced
one position to the right.. Exactly the saas procedxrre is followed in RII.

<!-- p. 27 -->
.
17.
Thus ^oth EI and EII shirt together. (Thare Is one exception to this
principle In on© of the terminal stepe of a multiplication but this
need not concern us here.)
The information stored In 2*'^ of EI la therefore shifted Into
2 . It is also retained in 2"*'^. If this digit is a 0, the sign of the
resulting quantity is and if it la a 1, the sign la 1. But this is
exactly the correct convention to ensure that the right shift is exactly
a division by 2.
The right shift operation can be performed n tinws (1 < n < kj)
by means of a single order.
This amounts only to an iteration n tiiaas of what la described
above
Since RI and EII ar« interconnected as ahown in Figure 1.5 above,
the Information shifted out of RI is tranaferred into RIIj but the naterlAl
shifted out of RII la loat.
We next discuss the division operation. To make precise what fol-
lowB we agree that the dividend is x, the division is y with -1 < x < 1,
-1 < y < 1, X < y
To describe the process we assume that the first 1-1 steps of the
division have been completed and that the first 1-1 digits q^, q , ...,
q._2 0^ ^^^ quotient Q are in positiona lK)-i, Ul-1, ..., 39, reapectively.
We also assume that y, the divisor, is in E and that the remainder r. -
is in B, We proceed inductively in this fashion:
.
(1) r^ = 2r^_^ - (sgn xy) yp^.^^/ r^ - x/2,
where

<!-- p. 28 -->
. .
18.
flgn r^_^ / 8gn (2r^_^ - (egn xy) y)
(2) P,., ^
•
1 agn r^_^ = egn {^^_^ - (agn xy) y)
PO'O
We next define q. aa
(3) '^i^'
li l-p^ agn xy = -1
We now show that
8gn rj_ - agn X, ( r^ j < | y [ .
We prove these Inductively. They are evidently true for i =. 1. We
show they are true for i + 1 auBauming they are true for i. If
agn r^ » agn^ (2r^ - (agn xy) • y)
then »
and
sgQ Tj^^j^ =• sgn r^ » agn x.
Next,
2r^ - (sgn xy) • y » 2 agn r^ • | r^ | - agn x • agn y • y =
= 2 sgn X • j r^ 1 - agn X • | y | - sgn x (2 ; r^ ; - i y )
Thus
'i+1 = «8^ 'i+1 •l^+l',"'8°^ -l^+l!" ««°» (2 r^ - y
and
<2
•l+ll - l^'il - ! yi lyl - ly! - !y
which completes the Induction in this case. In the contrary case
^+1 ' ^i'

<!-- p. 29 -->
19.
and
sgn X -- 8gn r^ ^ sgn {2t^ - (egn xy) • y) - sgn x • 8gn (2 ) r^j - ', y| )
Thus
Bgn (2 \t^\ - i y ; ) = -1,
i.e.
and sgn r . = sgn 2r. = sgn r = sgn x, since 2r is in the nachine's
number range. Hence v« have proved our induction.
We multiply both aides of (1) by 2~ and sum for i = 1, 2, ...,
n. We find
2"^"^"^^ r^ = 2\q - (sgn zy) y P,
where
°-^
-i
1-0
Thus
(k) X =» (sgn xy) P • y + R
where
since 2 r = x.
If sgn xy = +1, (^) beconwB with the help of (3)
X = Q y + R,
where
n-1
Q - 2"^ q^ - P.
i=0
If sgn xy = -1, then
Q = n E -1 2"^. q, = n : - ? 1 2-^ • (l-pJ - 2 - P) - 2 _ ° n+ * l S
i:«0 1-0

<!-- p. 30 -->
i.e. apart from the term 2"^"^" ' Q ie the complement of P. Thus our
quotieat is wroug in the last place.
Up to this point wo have made no mention of "rounding' proceduree.
We do not wiah iu this place to discusB the theoretical background of
such procedures. Instead we merely call the reader's attention to such
a discussion in a previous report ' and state the rules ve have adapted.
In the multiplication operation a digit is added to 2 and the result
truncated after 39 digits after all carries have been completed. In the
division operation we perform 39 steps determining the sign and 38 infornB.-
tion digits. The 39th such digit is automatically made 1.
We complete our discussion with a discussion of the roles of RI^
EII, EIII during the division operation.
At the start of this operation the dividend is in BI, the divisor
is in RIII. Although left shifts are to be performed the channel from
HI to RII which normally transmitts for a left shift is suppressed. In-
stead the quotient digits are inserted seriatim into position 38 of BII
and shifted left. The operation continues until the sign digit of the
quotient reaches position of EII. At this time the remainder is In EI.
It remains only to explain how the machine makes the discrimlna-
tidna indicated in (2), (3) above. First we note that In (2) the expres-
sion "sgn r -" can be replaced by sgn x. Thus (2) becomes
1) Preliminary Discussion of the Logical Design of an Electronic Comput-
ing InatrumBnt, Burks, Goldstine and von Neumann, Pt. I, Vol. I,
I9k6, pp. 19, ff-

<!-- p. 31 -->
.
Ji.
fO aga X ^ sisa {^^_-^ - (agn xy) y)
(2') Pi-1
1^1 agn X = agn C'^^_-j^ - (agn xy) y)
It was not convenient engineering-wise to detect the slgnum of
2r^_^ - (sgn xy) y and therefore a aomevhat different quantity was ob-
served. To explain this we suppose for the moiaent that
s = 2r^_j^ - (agn xy) y
is expressed not as
.(r^+^/2+^/22
8 + ... ^ ^n-l/^""'^
hut as
8 . (T_^ + y^ . Cj/22 + ... + \J2''-^.
I.e. we regard not as a sign digit hut as an arithmetic digit and
. aa the sign digit. The convention adopted is now thla:
(1 - sgn x)/2 - r_^
(2") Pi.i =
,
! 1 (1 - sgn x)/2 / 6_-^-
It la not difficult to see that conventions (2') and (2") are equivalent.

<!-- p. 32 -->
.
22.
II. THE ORDERS
We proceed now to an explanation of each order in terms of the
contents of RI, BII, RIII and of certain other facta relevant to the
coder. It is desirable first, however, to mention the digital structure
of the orders
Each order consists of 20 binary digits, the first 10 of vhich
usually specify a Memory location and the second 10 of which specify
the operation to be performed. Two orders are grouped together into a
single kO digit word. The Control is so arranged that it first executes
the left-hand one of the pair and then the ri^t-hand one. These are
referred to as the first and second phases of the order-word, respec-
tively. In what follows we number the digits of an order throu^ 9
for the Memory location and 10 throu^ 19 for the operation.
We now describe the orders.
0.1. TEE PID6 CIMB ORDER.
a) This order may be in either the first or second phase
of an order-word.
b) The digits 0-9 (20-29) express the Memory location
from which operand is to cone.
c) The so-called step-digit, digit 11, may be a or a 1.
In either case the order is executed. In the former case the Control is
prevented from proceeding to the next order and the nachlne stops. If
after the stop the step digit is changed to a 1, the order Is re-done
and the machine proceeds normally.

<!-- p. 33 -->
.
23.
d) At the start of the order the contents of the
registers are:
R- Irrelevant
R irrelevant
R3
Irrelevant
z b, the addend
•
e) At the end of the order the contents of the regis-
ters and of memory location x are:
«1 ^
R unchanged
r3 b
X b
0.2. THE PLUS HOLD CRDKR
a), b) , c) The same as for 0.1.
d) At the start of the order the contents of the
registers and z are:
R^ a, the augend
R_ irrelevant
R irrelevant
z b, the addend.
• e) At the end of the order the contents of the regis-
ters and z ejre:
R, a + b
R unchanged
s} b

<!-- p. 34 -->
.
2k.
0.3. TEE MmUS CLSAB ORDSR.
*) > ^), c) The same aa for 0.1.
d) At the start of the order the contents of the
regiatera and x are:
E- irrelevant
Ep Irrelevant
R"^ irrelevant
X b, the subtrahend
e) At the end of the order the contents of the regis-
ters and X are:
Ej^ 2 - b
E irrelevant
B^ b
X b
0.4. THE Minus HOLD CEDEK
a), b) , c) The same as for 0.1.
d) At the start of the order the contents of the
registers and x are:
E. a, the mlnuand
Ep irrelevant
B irrelevant
X b^ the subtrahend
e) At the end of the order the contents of the regis-
ters and X are:
E^ a - b

<!-- p. 35 -->
.
i>-
B unchanged
X b
0.5- THE pure ABSOLDTE CLKAB QRDKB
^)> ^)) o) ^0 BBLffle as for O.l*
d) At the start of the order the contents of the
registers and x are:
B- irrelevant
B irrelevant
B irrelevant
X h, the addend
•) At the end of the order the contents of the regis-
ters and x are:
IM
«!
Bp unchanged
r3 b
X b.
0.6. THE FLOS AB80LDTE HOIi) QRDIR.
a), b), o) The same eia for 0.1.
d) At the start of the order the contents of the
registers and x are:
B. a, the augend
B_ irrelevant
B irrelevant
X b, the addend
,

<!-- p. 36 -->
-
-6.
e) At the end of the order the ooatenta of the regie
ters and z axe:
Bj_ a + b
t 1
B Unchanged
B^ b
0.7- THE MIHUS ABSOLDTK CUKAR ORDlffl.
*)/ ^) } c) The eaiBB as for 0.1.
d) At the start of the order the contents of the regie-
tera and z are:
R Irreleyant
R irrelevant
R irrelevant
X b, the eubtrahend
e) At the end of the order the oontents of the regis-
ters and z are:
\
2 - b
1 1
R unchanged
B^ b
X b.
0.8. THE MIHUS ABSOLDTB HOLD ORDER.
a), b), o) The sane as for 0.1.
d) At the start of the order the oontents of the
registers and z are:

<!-- p. 37 -->
£7.
R.. &, the minuend
E irrelevant
R3
irrelevant
I b, the subtrahend
e) At the end of the order the contents of the registers
and X are:
R, a - b f
H^ unchanged
R3'b
0.9. THE KtJMIPLT IfO-RODND OFF ORDK.
a) The same as for 0.1.
I
b) The digits 0-9 (20-29) express the neBory location
from vhlch the multiplicand is to coma.
c) The step digit is as in 0.1. The clear digit 18(38)
may be a or a 1. In the former case the contents of RI at the start
of the order vill be added to the first partial product. I.e., if c is
in RI at the start and if the desired product is a b, then vhat is pro-
-39
duped In this case is ab ^ 2 d. In the latter case the contents of
RI are cleared to at the start of the multiplication.
d) At the start of the order the contents of the regis-
ters and X are:
R irrelevant if "clear"
R a, the multiplier
R-^ irrelevant
z b, the multiplicand.

<!-- p. 38 -->
)
28.
e) At th« end of the order the contents of the regis-
ters and X are:
\ =0' °1' "' ^^39
"'
=- -^0' ''l' ^39' ""^^ '"' °78 ''^^o ^'
the eiga digit of b. (We ueuns the "clear"
case
•
B^ b *
X b.
0.10. THB MULTIPLY BOOND-OtPT CRDBR.
a), b), c) The eaoe qs for 0-9.
d) The saoe as for 0.9-
e) At the end of the order the contents of the regis-
ters and x are:
^1 ^0' ^1' ^2' '"' ^39
Bg d-V' °ko * ^' ^1' -'' ^78' ^"^ ^0'
"' ''39'. ""^vo* "l*!' ••*' ''tS^ ° ^ •
b3 b
X b.
0.11. Tfflt DIVISION OHDEB.
a) The same as for 0.1.
b) The digits 0-9 1[20-29) express the memory location
from which the divisor is to come.
c) The sane as for 0.1.

<!-- p. 39 -->
29.
d) At the start of the order the contents of the regis-
ters and z are:
Rj^ H, the dividend
Bg Irrelevant
B3
Irrelevant
z B, the divisor.
e) At the end of the order the contents of the regis-
ters and z are:
B. ^, twice the remainder
"'
*2 '"o' '^l' ^38' ^' °^' C*^P**' ^
B^ D
z D
0.12. TEE LOAD BIT ORDXB.
a), b) The same as for O.l.
c) The same as for 0.1. If the clear digit Is a 1,
then B. Is pre-cleared to 0.
d) At the start of the order the contents of the regis-
ters and z are:
B- Irrelevant
Bp Irrelevant
B3 Irrelevant
z b
e) At the end of the order the contents of the regis-
ters and z are:
B. Unchanged if clear digit Is 0; If clear
digit Is 1.

<!-- p. 40 -->
30.
«2 ^
z b
.
0.13. THE STOKE ORDKB.
a) The sane as for 0.1.
b) The digits 0-9 (20-29) express the Mmory location
Into which the contents of BI are to be placed.
c) The step digit muBt always be a 1. Thus the store
order cannot be used as a stop order.
d) At the start of the order the contents of the regis-
ters and X are:
B^ b, the word to be stored
Bp irrelevant
R3
irrelevant
.
X irrelevant
e) At the end of the order the contents of the regis-
ters and x are:
»1 ^
B Unchanged
B^
X b
O.l^V. TEX STOBI CLKAB GBSSR.
a), b), c) The sane as for 0.13*
d) At the start of the order the contents of the regis-
ters and X are:

<!-- p. 41 -->
31.
R. Irrelevant
B Irrelevant
E3
Irrelevant
z Irrelevant
e) At the end of the order the oonteott of the regis-
tera and z are:
(
Hj^
B Unchanged
H^
z
0.15. and 0.16. THE UHCOiroiTIOHAL TRAMSFKR QBDERS.
a) The sane as for 0.1.
b) The digits 0-9 (20-29) ezpress the Bemory location
to which the control la to be transferred. I.e., the location where
the nezt order is to be found.
c) If the step digit is a 0, the control transfer takes
place to the same phase of the new order-word as that of the order in
question. If the step digit is a 1, the transfer takes places to the
opposite phase.
d) At the start of the order the contents of the regis-
ters and z are:
E, Irrelevant
Rp Irrelevant
R-' Irrelevant
z b; the nezt order-word

<!-- p. 42 -->
3a.
e) At the end of the order th« contente of the reglrters
and X are:
R Unchanged
Bg Unchanged
B^
E3 b
X b.
0.17. and 0.18. TBS CONDITKniAL TRAHSPTO CBDKR8.
m
a), b), c) The aana for 0.I5 - 16.
d) At th« start of the order the contents of the regis-
ters and X are: * '
Case A Case B
Rj_ a > Bj^ a <
B Irrelevant B_ Irrelevant
B3 Irrelevant B" 3 ^ Irrelevant
X b, the next order-vord X b, Irrelevant
e) At the end of the order the contents of the registers
and X are:
Case A Case B
B. Unchanged B. Unchanged
Bp Unchanged B Unchanged
B^3 a3 b
R3 b B. Unchanged

<!-- p. 43 -->
33.
0.L9. THE QUICK-SUM OPDKR.
a) The order may be only In ths flrat phaae of an order-
word.
b) The digits 0-9 express the memory location x from
which the flrat operand Is to come. It la obtained from the orders
0.1. - 0.8. , inclusive, by setting digit 19 to 1. In this case the
order specified without this digit being 1, i.e. one of the set 0.1 -
0.8, is performed first at the location x and then serially at each fol-
lowing location through 1023 after which the order terminates. The sec-
ond phase order must be a transfer of the control to the location of the
next order-word. This la due to the fact that the order counter no
longer stores the location of the next order-word.
c) The step digit must be a 1.
d) At the start of the order the contents of the regiatera
and X are;
K Irrelevant
E3
Irrelevant
X + 1 b^ 1 « 0, 1, ..., 1023 - X
e) At the end of the order the contents of the registers
and X are:
^'^°''
^1 \023 '' ''^'
^
a + f{\^^) if 0.2, k, 6, 8
R Unchanged
«^ ^023
X + 1 bj^,

<!-- p. 44 -->
where

    f(b) =  b       if 0.2
           -b       if 0.4
           |b|      if 0.6
          -|b|      if 0.8

0.20. RIGHT SHIFT, NO-ROUND OFF ORDER.

a) The same as for 0.1.

b) The digits 4-9 (24-29) express the number of shifts to be executed.
This number n is expressed as an integer times 2^-9 (2^-29). The digits
0 - 3 are irrelevant. The number stated in digits 4 - 9 (24-29) must not
exceed 47 and must not be 0. (A shift by 0 is executed as a shift by 1.)

c) The same as for 0.1.

d) At the start of the order the contents of the registers are:

    R1   a0, a1, a2, ..., a38, a39
    R2   b0, b1, b2, ..., b38, b39
    R3   Irrelevant

e) At the end of the order for a shift of 1 the contents of the registers are:

    R1   a0, a0, a1, a2, ..., a38
    R2   a39, b0, b1, b2, ..., b38
    R3   b0, b1, b2, ..., b39

For a shift of n this is iterated n times.

f) This order may be given with the clear digit, digit 18

<!-- p. 45 -->
35.
(38), a or a 1. The situation above ahowa the ceae of thla digit - 0.
We show below the caae when It is 1.
e') At the end, for a shift of 1, the contents of the
registers cure:
R 'a , 0, 0, 0, ...,0
^
Hg 0, b^, b^, b^, ..., b^Q
B bQ, b^, bg, ..., b^^
We note that even though E has been cleared to before the shift
starts the sign of the nun4)er that was there la propagated by the shift.
0.21. BICHT SHIFT, BOUND OFF ORDKB.
This order Is not yet available.
0.22. LEFT SHIFT ORDER.
^)} ^) ) c) The same as for 0.20.
d) At the start of the order the contents of the regis-
ters are:
^1 *0' ^1' *2' "' V *38' *39
^2 \' \' ^2' •••' ^39
B Irrelevant
e) At the end, for a shift of 1, the contents of the
registers are:
^1 *^i' ~2' •••' "38' "39' "0 •
^2 ^1' ^2> •"' ^38' ^39' *0
R^ b^, b^, ...,b3Q, b3^
For a shift of n this is Iterated n times.
f) This order may be given with the clear digit a or a 1.

<!-- p. 46 -->
.
36.
The situation above shove the case of thl» digit » 0. We show below
the oaae when it is 1.
e') At the end, for a shift of 1, the contents of the
registers are:
B^ 0, 0, ..., 0, 0,
B^ b^, b^, ..., b^Q, b^^,
B b^, b^, ..., b3^, b^Q, b3^
g) We indicate next what occurs when a left-shift (of 1)
Is followed by a right shift (of 1)
e") At the end of the order the contents of the regis-
ters are:
^1 *0^ *1' *2' •••' '38' *39
Bg 0, bj, b^, ..., b^Q, b^^
B b^, b^, ..., b^^, a^
0.23- THZ B TO B. CEDER.
a) The same as for 0.1.
b) This order is actually not one but a set of eight dif-
ferent ones. These are essentially the orders 0.1. - 0.8. except that
the operand cones not from a memory location x but rather from BII. One
other feature is available in connection with this order. To describe
0-3
this we consider the digits 0-9 (20-29) Of these (20-23) are Ir-
•
relevcmt. The digits k - 9 (2^-29) are as indicated in b) of 0.20. They
express an integer tines 2'^ (2"^^) which is > and < U?.
c) The same as for 0.1.
d) At the start of the order the contents of the regis-
ters are:

<!-- p. 47 -->
37.
E. a
K3
Irrelevant
e) At the end of th« order the contents of the regla-
ters are:
r
i2g(a) + (n+1) f(b) If n is odd
) g(B) + nf(b)/2 if n is even,
where f Is defined in the discueaion of Order 19 and
Ta if 0.2, \, 6, 8
g(a) - I
Ji if 0.1, 3, 5, 7
^2 ^
?} b.
0.2l^, and 0.^5- IBM AND ERDM EEIMING QRDKB.
a) These orders must be second ph&ae ones. Their use is
to specify the nuinber of cards to be read or punched by the IBM repro-
ducer or the starting word block number and the number of such blocks to
be loaded or unloaded on or from the drum.
There are 12 words on an IBM card oooupying the coluBins 1-^, 6-9>
11-lU, 16-19, 2l-2i*, ^-29, 31-3^, 36-39, 'l-W*, KG-k9. The colums 5,
10, 15, 20, 25, 30, 35, 1*0, ^5 are never used. Coluana 66-80 are used
for identifying information for the human operator. Each word occupies
a row on ths card, a hole indicating a 1, no hole a 0.
The Magnetic Drum contains 20^8 words divided into two main
groups of 1024 each. Each of these is composed of 32 blocks of 32
words each.

<!-- p. 48 -->
38.
b) The address portion of tha order Is used to specify
the number of cards In the case of IBM operation or the starting block
number and the nuniber of blocks in the case of drum operation. In the
former case, the IBM one, the digits 20-22 are irrelevant; 23-29 ezpress
-29
as an Integer times i. ' the number of cards to be processed. In the
latter case, the drum one, the digits 20-2U are used to express the start-
Ing block nuniber as an integer times 2 ; the digits 25-29 the number of
blocks to be processed, the number being an integer times 2" . It is
important to note that the blocks and the number of blocks are counted
1, 2, ..., 32. Thus 00000 means block 32 if it appeans in positions 20-
2U and means 32 blocks if in 25-29.
c) It le best always to put a step-digit, digit 30, into
this order.
In principle this is not one but a set of l9 orders, 0.1 - 0.l8;
it differs from these only in that the address portion does two things:
It is 'not only the operand for the order 0-1 - 0.l8 but Is also sent to
a special register in the IBM-Drum Control. It remains there permanently
until altered by another such order.
Since the analogous 0.1 - O.lS order will be executed using the
given address aia operand it will bring an irrelevant q,\iantity into the
Arithmetic Unit. Thus if the contents of BI are relevant and it is
desired to prime, It is best to use a load K type of order, whereaa
if the contents of RII are relevant, one of the type 0.1 - 0.8. The
priming order differs from 0.1 - 0.l8 only in that digit 31 is a 0.
0.26. IBM INFUT TO MBMOBT ORDER.

<!-- p. 49 -->
39.
a) This nuBt be flrat phaie. The second phase of the
«»
order-word must be a transfer of the control to the next order-vord.
b) The digits 0-9 are used to specify the Beaory loca-
tion X for which the order is first executed. The order Is then executed
for X + 1, X + 2, ... until the number of cards previously set by the
prior priming order has been reached.
c) The step digit mist be a 1.
d) The only register tha,t Is unchanged Is RII.
0.27- IBM OUTPUT TO MBMQRY ORDER.
a), b)^ c) The same as for 6.26.
d) All registers are altered.
0.28. DRUM HTFDT TO MEMORT (BCER.
a) The same as for 0.26.
b) The digits 0-9 are used to specify the mamory loca-
tion X for which the order la first executed. The order Is then exe-
cuted for X •» 1, X -t- 2, ... until the number of blocks previously set
by the prior priming order has been reached.
c) The same as for 0.26.
d) The saas as for 0.26.
e) The drum stores 102l<' bits per track and has 60 tracks.
These 80 are divided Into 2 sets of ^fO each which constitute the major
groups mentioned above In the discussion of order 2k. The selection of
the proper group Is controlled by digit 15 . If It Is a 0, group A Is
selected; If It is a 1, group B Is selected.

<!-- p. 50 -->
ko.
0.29. DRUM OUTPDT FROM MEMORT OKLKR.
a), b) , c) The saoa aa for 0.^6.
i) ThA saiBB aa for O.27.
e) The scum aia for O.ciS.

<!-- p. 51 -->

![Digital representation of Orders — order code table](images/table_orders.jpg)
*Digital representation of Orders — order code table*

The digital representation of St
Arlth
ORDERS No Ext.

<!-- p. 52 -->

![Fig. 1 — Eccles-Jordan toggle circuit](images/fig_01.jpg)
*Fig. 1 — Eccles-Jordan toggle circuit*

*^
lU. CIBCniT EIZMSKTB
Before proceeding to describe the organization of the vaxlous orgems
of the cooqputer In detail, ve vlll first gl7e a brief dlsciiaslon of sone
basic circuits which occur repeatedly.
First, and most Important, Is the familiar Sccles-Jordan circuit,
the form used being Illustrated In Fig. 1. This vlll alvaya be referred to
as a "toggle".
ii/(i i/zota
Fig. 1.
A and B designate d. c. buses: these are held at -fl^Or except vhen clear-
ing action Is desired, vhen the appropriate Toltage Is dropped to -t-^Ov, this
vlll be discussed belov.
The circuit Is so designed that satisfactory operation Is obtained If
the resistor values do not vary more than lOft from their acmlnakiv&lues and
the tube characteristics remain vlthln the region vhere the ordlnates lie
I

<!-- p. 53 -->

![Fig. 2 — Conventional toggle symbol](images/fig_02.jpg)
*Fig. 2 — Conventional toggle symbol*

H3.
between ^Oft and 200)1 of their noolnal Tallies.
If nominal values of the resistors are used, ami the 6j6 character-
istics as given by the manufacturer, the follovlng electrode voltages ob-
tain:
"on" grid +»5t
"off" grid -kCnr
"on" plate +35v
"off" plate +100V
S "on" grid current .Soa-
A conventional representation of the toggle circuit Is sonetlmes
convenient: the bne given In Fig. 2 vlll sometimes be used
Pig. 2.
The toggle Is a binary device. In the sense that at all tines one
section of the 6j6 Is In a conducting state, while the other Is not. It
Is merely a matter of convenience which one of the two states Is chosen to
represent a binary 0, the other then necessarily representing a binary 1.
In order to represent vlsxially the contents of a toggle, a neon bulb Is con-
nected from the plate of the section that Is off when the toggle Is holding
a 1 to ground. Clearly this bulb lights up to represent 1, while It Is off
when the toggle holds 0. Thus In Fig. 1 we have adopted the convention that

<!-- p. 54 -->
kk.
the toggle holds a 1 vhen the left-hand section Is non-conducting.
We nov consider the "clearing" action, assuming the given convention
as to the contents of the toggle. Suppose the toggle to hold a 0, and let
bus A drop to +^0t, while B reaains at -i-l^Ov. The grid voltage of the right
section is merely reduced still further. Hence that section renains exit off,
the grid voltage of this left section is held up, and the state of the tog-
gle does not change. On the other hand, if bus B is dropped to -i-^Ov, while
A is DBintained at -fl^Ov, the grid voltage of the left-hand section is re-
duced below cut-off, and the toggle is changed to its other state. Siailarly,
if a 1 is held, dropping B to +50v while holding A at +150v has no effect,
while dropping A to +^0v while holding B at -t-l^Ov changes the state of the
toggle.
Putting this differently, the operation of dropping A to +50v while
holding B at -t-l^Ov guarantees that the toggle will subseciuently hold a 0,
while holding A at -fl^Ov and dropping B to -i-^Ov guarantees that it will
subsequently hold a 1. Thus these operations are respectively referred to
as "clearing to 0" and "clearing to 1". The clearing action is produced by
pulsing the appropriate bus. With the present toggles, it is necessary that
the bus voltage should renain below -fTOv for approziaiately one microsecond
to produce the desired clearing.
In a few places in the computer, it is desired to use a toggle which
^
requires a shorter time to change from one state to the other. In these ap-
plications a so-called "super-toggle" is used, which changes its state in
half the time required by the ordinary toggle. The circuit is given in
Tig. 3.

<!-- p. 55 -->

![Fig. 3 — Toggle-setting circuit](images/fig_03.jpg)
*Fig. 3 — Toggle-setting circuit*


![Fig. 4 — Gate circuit for setting toggle A to match toggle B](images/fig_04.jpg)
*Fig. 4 — Gate circuit for setting toggle A to match toggle B*

ZZO
-f
—3oo
Fig. 3.
It has been shewn hov a toggle may be set In a desired state, or
"cleared". It Is also necessary to be able to set a toggle Into the saas
state as another toggle: that Is, given togglesA and B, It Is necessary to
provide a mechanism which guarantees that, after some definite time, the
contents of A are identical with those of B. This is readily accoiq>lished
by means of a gate circuit as shown in Fig. k.
±
Fig. U.

<!-- p. 56 -->
Jt6.
Th* tube \iB*d h*re Is oaa 8«ctlen •t a 6j6, vlth cathode noroally
Baaintained at +10v. When it is desired to transfer inTorination from B to
A (note that the given circuit permits a transfer to be made only in this
direction), the cathode of the gate is dropped to Ov. The gate cannot
conduct while its cathode is held at +10v, as its grid cannot be above
about + .5v. Let us uae our eaurlier convention as to the representation
of binary O's and I's by states of the toggle. If B holds a 1, cleeurly
nothing can happen vhen the gating signal arrives at the cathode of the
gate, as this tube must remain cut off. If, on the other hand, B holds
a 0, conduction takes place when the cathode of the gate falls to Ov, ajad
plate current, flowing through the plate load resistor of the left section
of A, will cause A to assume the state representing 0. The gate thus
guarantees that if B holds a at the time the gating signal is applied,
A will be caused to hold a 0. Suppose now that before the arrival of the
gating signal, A is cleared to 1. Then if B holds a 0, the gate causes A
to assume the state, while if B holds a 1, the ^te has no effect, and
A continues to hold a 1. Thus the sequence of signals "clear A to 1" and
"open gate into A", results in A holding the sane Information as B.
We also note that if the gating signal were made sufficiently nega-
tive, enou^ grid current could be drawn by the gate to cause a change of
gtate in B. This effect is not u«ed in the present design, but could con-
ceivably be useful.
The gate circuit as described is a coincidence device, equivalent to
the formation of a logical product. Other methods are used in parts of the
machine; for example, consider the circuit of Fig. 5 where the signals ap-
plied to the grids assume the levels of +10v or -lOv. This is a cathode
I

<!-- p. 57 -->

![Fig. 5 — Cathode follower](images/fig_05.jpg)
*Fig. 5 — Cathode follower*


![Fig. 6 — Two-diode gate circuit](images/fig_06.jpg)
*Fig. 6 — Two-diode gate circuit*

^,
follower, euad the cathode will follow the hi^iest grid. Thus the cathode
voltage will assume the lower level if and only if both grid voltages assvune
their lower levels.
Fig. 5.
Another gate circuit which will be found in the computer aakes use
of two diodes connected as in Fig. 6. (see for ezaaple WG 1325).
Fig. 6.
In one particular case A assunes one of two levels (-t-lOv, ;,-^0v) and B also
one of two levels (+10v, -lOv). The voltage at C will always be slightly
above that of the lower cathode, and hence will assusne a hig^ value (slightly
above -i-lOv) only if both A and B sinultaneously attain their hi^ier values.

<!-- p. 58 -->

![Fig. 7 — Gate symbol](images/fig_07.jpg)
*Fig. 7 — Gate symbol*

>•#.
• Usually we think of cme input to a gate as an enabling signal, which
places the gate in a condition to pass on the other input. A convenient
symbol for a gate is given in Fig. 7,
^
-^-c
Fig. 7.
Vhere A and B are the inputs emd C the outpizt; the enaibling signal is B.
Sonetimes it is convenient to use a solid arrcwhead for a static voltage,
and reserve the open eu:*rowhead for a voltage pulse.
Cathode followers are found in considerable nuniberB. These are used,
for example, to drive a nxxaber of gates of the type illustrated in Fig. k,
and in other places where it is necessary to supply a ccosiderable amount
of cixrrent from a lew impedance source. The cathode followers are ordinar-
ily operated in that region of the characteristics, where sufficient plate
cxirrent is drawn to cause the cathode voltage to rise slightly above the
grid voltage, so that no grid current flows. For purposes of ordinary anal-
ysis, we shall commonly assume that the cathode voltage is exactly the same
as that of the grid, the cathode rise being neglected. This will ordinarily
not lead to any difficulties. »

<!-- p. 59 -->
Hp«
If. 1SB ABrCSMETIC dtOAN
THE BSGISTSKS
A Beglster Is essentially nerely a device vhlch serres as the reposl-
tarj of a single vord of aachine language. The tern Is usually used to
designate a storage device the contents of vhlch are directly available
vlth very slight delay. Thus In a nachlne vhoee language consists of forty
bit vords, a set of forty toggles foms a convenient Beglster. Hovever,
are storage of Infoanaatlon does not suffice, as the Beglsters which are to
serve ais the Accuaolator emd the AB and SB Beglsters of the nachlne mst be
capable of other functions. These devices must be able to transmit and re-
ceive Inforoatlon, and to perform shifts (at least for certain purposes) of
the Infonaatlon to the left or to the rlg^t.
The tsansBlsslcn of Infaraatloii Into or out of a Beglster consisting
of toggles Is readily acco^llsbed by the gating circuits that have already
been discussed, vhlle the slngple aeans by vhlch toggles can be cleared to 1
or to have also been described.
In perfoxvlng the shifting operation. It Is desired that the Infcfraa-
tlon should never exist as aerely transitory electric or oagnetlc fields,
but should rather at all tlaes exist In static form. An effective method
of acconpllshlng this Is as follovs: tvo rovs of toggles are provided-la
the Beglsters of the nachlne the tvo rovs (upper and Icwer) In Beglster BI
are called B and B^, and similarly for the other tvo Beglsters-and gates
are arranged vhereby the Information held In a toggle of the lover row Is
transmitted to the left or rl^t In tvo steps: first, up to the correspond-
ing toggle of the upper rov, then second, from this toggle dovn to the left

<!-- p. 60 -->
^
or to the rl^t. Fig. 8 shcxra hov this Is dcoa: It represents the coluMns
n-1, n, and n-»-l of the Begister.
Tvo gates lead up froa each toggle of the lover rov to the toggle In
the corresponding position of the upper row, vhile frca each toggle In the
upper row a gate leeuLs down to the toggles In adjacent coluams of the lover
rcw. The gate G(reen) can transait a up, while T(ellov) can transnlt a 1.
Hence to assure the traunsalssloaa of the nuoiber In the lover rov of toggles
to the upper row, tvo altematlye procedures are at our disposal: the top
rov aay first be cleared to and then the Tellov gates opened, or the top
rcw nay be first cleared to 1 and then the Oreen gates opened.
To shift the nuaber new standing In the top rcw of toggles back down
to the lover tcm. In such a vay that the resulting contents of the lover rem
vlll be the nuniber that originally resided In that rov, but shifted one place
to the rl^t or to the left. Is the function of the gates B(ed) and B(lack).
Por the rlf^t shift, the Black gates alone are available: from the diagram.
It Is clear that these can transmit only I 's
^
so that It Is necessary first
to clear the lover rcw to O's before opening the Black gates. For the left
shift, the Bed gates can transmit coly O's, so It Is necessary first to
clear the Icwer rem to l*s.
It vas shown In the dlscuaslon of gates, that It Is quite possible
to cause a gate tube to clear the toggle from vhlch It transmits Information.
Thus the Oreen gates could be used to clear the toggles of the bottom rov to
I's, vhlle the Tellcw gates could be used to clear these toggles to 0*8.
Similarly, the Bed gates could be used to clear the toggles of the upper
rov to I's, vhlle the Black gates could be used to cleecr these toggles to
O's. Althoii^ this property of the gate tubes Is not exploited In the

<!-- p. 61 -->

![Figure 8 — Clear-gate chassis interconnections](images/fig_08.jpg)
*Figure 8 — Clear-gate chassis interconnections*

^ ^ H.
Cy «D
-
0^
-J i
—
I ^/vv«»/> • » ''WWtf' <
MMN^^* 4
I »vv»«^ %

<!-- p. 62 -->
».
present Bachlne, It neyertheless prorldes a coorenlent Mumer of designating
the Tarloxis clear operations. Thus a clear vlll be described bj the color
used to designate that gate vhlch could be used to iwrfans the clear. The
follovlng table shews hov the color code Is used to describe the various
shift and clear operatims:
Bed: Shift left down zero
Clear top to one.
Green: Shift up zero
.
Cleeu: botton to one.
Tellov: Shift up one
Clear Bottom to zero.
Black: Shift right dovn one
Clear top to zero.
In this teralnology, the process of shifting rl^t one place consists of
the follovlng operations: Black clear, Tellov gate^ Tellov clear. Black
gate. The left shift is described \>j: Black clear, Tellov gate, areen
clear. Bed gate. In each case, of course, there is an altematiye process
ayailable vhlch nakes use of the Oreen shift up.
The structure of a forty stage Shifting Begister follovs directly
tram, the diagram of the three stages vhlch has been discussed. The actual
Shifting Beglsters in the machine all differ in certain details from the
one described, vhlch may be thouf^t of as an archtype. It Is clear that
means must be provided by vhlch Information can be Inserted in or extracted
from the Beglsters. This Is done by changing certain of the coonections to
the gates. Beglsters BI and BII remain Shlftioig Beglsters vlth these special
comMctions. Bill, on the other hand, should not be thou^^t of as a Sl^i^ing
Begister at all. The tvo rovs of toggles In Bill actually form tvo independ-
ent Beglsters, vhlch form part of the means of coBnunlcation betveen the
! ^

<!-- p. 63 -->

![Fig. 9 — Register chassis tube layout](images/fig_09.jpg)
*Fig. 9 — Register chassis tube layout*

»*
VllllamB Memory and the rest of the machine. Also a small amount of addi-
tional equipment 1b associated vlth the various Beglsters. In the Interests
of clarity, each of the three Beglsters vlll be Vrlefly discussed and the
Interconnections vlth the rest of the machine Indicated.
All three Beglsters consist physically of four chassis^ each of
irtiich contains four rovs of tubes, laid out as follovs:
o

<!-- p. 64 -->
BI and BII are Identical except for certain clrctilts exterior to the
Beglster Chassis: these vill be described later. A schemtlc Is glren In
DWG lo. 1322. It has already been observed that RIII Is not a Shifting
Beglster at all. It actually consists of tvo Beglsters and associated gate
tabes by oeans of which infonatlon can be Inserted In B^ and Bo: for a
schraatic, see IMG lo. 1323> in which the top row of tabes shown are the
Coiqpleaent Gates used to read out to the Adder, and are not actually aounted
on the Beglster Chassis. Despite these differences, it is convenient to use
the saae noaenclature for the gate tubes of all three Beglsters. In all
cases, the row of tubes directly below the toggles of B are alternately
froB the left end of the chassis Bed aiid Black gates, while those of the row
below are alternately Yellow and Green gates. Bach gate tube, being a 6j6,
contains two gates. (Wote that the two center colunns in each scheaatlc are
occupied by Qate Drivers. Bote also that in each top row of toggles the con-
veirtiOQ is that Is signified by conduction of the left section, while In
the bottom rev the opposite is true.) As to the physical arrangeasnt of the
gates, the Bed g»te froa coluan n to coluan n-1 is in coluan n, while the
Black gate to colum n froa coluan n-1 is In coluan n-1, n signifying as before
A
the first coluaa in anyBeglster Chas . Fxirthemore, the Yellow gate between
the toggles of coluan n-1 is physically located In coluan n. Thus in a coa-
plote forty stage Beglster, it is necessary to provide a Yellow gate for the
39th coluan, while half of the Yellow and Bed gate tubes of coluan 0, and
half of the Black gate tube of the 39th coluan aire not actually used within
the ko Beglster stages, and hence are free for other uses: we shall see
what advantages are take<n of these circuastances when we exaalne the "end-
around" cirexxlts.

<!-- p. 65 -->
55.
Now let us exaaiine the actual uaes of tha gate tubes. In RI and
BII the Bed^ Black, and Tellov gates are connected and used exactly as In
the archetypal Shlftlxig Register already deaorlhed. The Green gates are,
1 2
hovever, used to transiBit information Into R and R from other sources:
1 2 ^
Into R from the Digit Beaolver, and Into R from R-^. In RIII the case
is quite differeiit, all gates being used for coBBiunication between the
Register toggles and bther parts of tha machine, according to the follow-
ing scheme:
(a) Yellow: into R from the Discriminator in the Williams
Memory.
(b) Green: into R-^ from R .
(c) Black: into R"^ from the Diacriainator in the Williaaa
Memory.
(d) Red: to Diapatch Counter and Control fromR^.
\Je have seen hcrw information is inserted in the Register toggles.
Outputs are taken as follows:
(a) RI: from right-hand grids of R toggles to Adder;
(b) RII: from right-hand grids of H toggles to RIII
Green Gates;
(c) RIII: (1) from grids of R"^ toggles to Adder via the
Coraplenent Gates;
(il) from left-hand grids of R^ toggles to RII
Green Gates;
(ill) from RIII Red (Jates to Dispatch Counter and
Control (already noted in the preceding

<!-- p. 66 -->
.
55a.
para^aph)
EI has certain other circuits associated with it. One of these
is an extra column to the left of the 0-th, in which the digit held in
the 0-th can be

<!-- p. 67 -->

![Fig. 10 — Extra column (end-around) gating](images/fig_10.jpg)
*Fig. 10 — Extra column (end-around) gating*

%.
held in the case of a left shift. Instead of being lost. The other is the
"end-around" arrangement, which, in the case of a right shift, transfers the
digit in the 39th colimn into the 0-tltfccolumn of B^*
The extra column is as shewn Ifl^the diagram. The tube used to provide
the Bed gate into the icwer toggle is mlready arailable in the 0-th coluaii,
vhlle half the Tellov gate tube of that column is available as a Yellov ^te
for the nev column.
BLRCk: CLBfita BUS
fZED Cl^EA/Z &US
SLACk: QaT£ conniYifiuo BUS
BLftcic <s/)r£ /juro 2
_
G££K/GfiTe
<i
corrrNifi)uo bus
finUi.T/PL/CfiiTlOU
,
yBLLow CLEaa aus
dGSEfJ "CLEae BUS
rc3 ^££)a^re /</
2"C<X.iJ/t7/tJ/U/PjT
**^ YELLO// <^fiTE //U Zrcoi-U/rtKI
2"/C. YELLOW QAre aus
t
Tig. 10.

<!-- p. 68 -->

![Fig. 11 — Black/Green gate diode arrangement](images/fig_11.jpg)
*Fig. 11 — Black/Green gate diode arrangement*

5T-
A Black gate is provided for rlg^t shift*. It will be noticed that a Oreen
gate la alao provided, which, unlike the other Oreen gates In BI, transmits
frcai the lover to the upper toggle of the new coIubq. The diode arrangeoant
also permits the transmission of Information froa the 0-th column of R^ to
the eozrespondlng column of B^.
BLACt CLEftQ
ffED CLEf^e
yetLoi^/(^atsco/nwAUD
YELLOtV cc£/ie
BLfict: (^/DTS Conor^AuD
rig. 11.

<!-- p. 69 -->
58.
The transmission of the overflow from the 3yth column of BI to
the 0-th column of RII Is elmplj talcen care of by tvo additional tubes:
One of these is a 2C>1 mounted just beyond the extreme right end of RI:
one section of this is used bb a Yellow Gnte for the 39th column of RI,
while the other is a cathode follower driven from one grid of the upi)or
toggle of the 29th colunn, and driving a wire which runs back to the ex-
treme left end of BII, as shown In Fig. 11. If ri^t shifts are ordered
in bo"t;h EI and RII, the toggle in the 0-th position in R will have been
cleared to before the Black Gate is opened. The opening of the Black
Gate will put into the 0-th stage of Rg * ^ ^^ a 1 was 'iel-<i in the upper
toggle of the 39th stage of RI, otherwise there will be no change. Thus
-S9 1
In any caae the contents of 2 E is shifted into the 0-th stage of R„.
See Fig. 11.
The performance of the clearing operations In RI and RII is the
function of the Clear Selector and Clear Driver Chassis: for each Regis-
ter there is one Clear Selector Chassis and four Clear Driver Chassis, one
for each of the types of clear operation used.
As the term indicates the Clear Selector Chassis determines which
clear Is to be performed. Fig. 12 shows half the tubes in the R Clear
Selector -- those which determine whether a Yellow or a Green clear is to
be performed. This circuit consists of a 6j6 twin trlode and a 6aL5 diode.
Hote that the cathode of the 6j6 is either at +10v or at -lOv, determined
by the Logical Control Organ of the machine, while the grids are at either
or -kOv. Thus as long as the cathode of the 6j6 Is maintained at +10v, both
sections of the tube will remain cut off, while the plate voltage will be
maintained at +150v by the 6iAL5 diode shown in the drawing. This is in turn
applied to the grids of a 6j6 Clear Driver cathode follower, whose

<!-- p. 70 -->

![Figure 12 — R1 Clear Selector (Dwg. A-1452)](images/fig_12.jpg)
*Figure 12 — R1 Clear Selector (Dwg. A-1452)*

<!-- p. 71 -->
60.
cathode in turn drives the gride of five 56B7 tube» connected In paral-
lel. The cathodes of these tubes are coxmectad to the clear bus, which
BuppllcB plate voltage to the toggles of R These tubes, therefore, again
.
merely form a cathode follower of lar^e current handling capacity. Wo,
therefore, eee that ae long as the 6j6 id the Clear Selector remains In a
cut off condition, the clear bus will be maintained at +150v.
Now let one of the grids of the 6j6 Clear Selector rise to Ov: to
be explicit, the left-hand one, the right-hand one remaining at -Uov.
Nothing happens as long as the cathode is maintained at +10v, because the
tube will remain cut off. Now let the cathode be switched to -lOv. The
left-hand side of the 6j6 will conduct, and the cathode will follow the
left-hand grid to Ov, thus holding the right half in a cut off condition.
Hence the rl^t-hand plate of the 6j6 will remain at +1^0 v, and the Green
clear bus will be maintained at this voltage. The plate of the left half
of the tube will, however, because of the plate current flowing through the
39,000 ohm resistor, fall to about 50v, which will cause the Yellow clear
bus voltage to swing down to this value also. Beverslng the voltages at
the two grids of the 6j6 in the Clear Selector will clearly cause the Yel-
low cleeur bus to remain at +I5OV, while the Green clear bus will swing down
to +5OV. Another set of two 6aL^'s and a 6j6 in the Clear Selector permit
the choice of Red or Black clear operations.
The voltages driving the grids of the Clear Selector are in this
example supplied from the Left-Bight (IR) Chassis since the choosing of
the Yellow or Green clear determines the concomitant right or left gating
operation.
The example discussed concerned the choice of the down path (diagonal;

<!-- p. 72 -->

![Fig. 13 — RII Gate Chassis](images/fig_13.jpg)
*Fig. 13 — RII Gate Chassis*

<!-- p. 73 -->
62.
—
H > BO 111 EI. Such a choice is alvajru T'recedet! by an up tranafer
(Hj^ --> R ) vhlch may be direct, I.e. Black,clear-Tellcw gate; or
throu^ the Adder, i.e. Fed clear-Green ^ate. This choice is funda-
mental to moat arithmetic orders; in particular, the diviaion scheme
1q based on a trial subtraction in ench step which le accepted If no
orerdraft results and rejected If It does. From this order has come
the terms: Accept meaning choose the Adder path, and Reject moaning
choose the direct path. This choice is determined for all orders by
the Accept-Reject Selector, drawing 0-1463.
In Figure 13 la shown the schematic of the Gate Drivers and Oate
Driver-Drivera. Each gate command is supplied by two cathode followers
In caacade: the first, which we shall call the Gate Driver-Driver, is
one section of a 2C51, while the driver Itself conalats of the two sec-
tions of a 5687 in parallel.
The Complement Gates permit gither the number in H'' or its one's
complement to be read into the Adder. These are shown in the top row
of DWG No. 1323' There is one 6j6 Complement Gate for each stage; every
five of these have their plates driven by two 5687's connected as shown.
Suppose the number in the toggle is a 0, the left grid being hl^, while
the right is low. The left and right grids of the 6j6 gate tube will be
then at about Ov and -1K)v, respectively. If the left grid of the 5687
is at +90v and the rl^t one at -30v, then certainly the cathode voltage
of the 6j6 will be Ov, signifying to the Adder. If these grid volt-
ages are interchanged, the 6j6 cathode voltage falls to a level of about
-kOv , signifying a 1 to the Adder. Thus, this arrangement permits us to
transmit to the Adder either the contents of B or its one's complement.

<!-- p. 74 -->
62a.
ADDER ADD THE DIGIT RESOLVKR
The iwrformance of the operation of addition ia the function of
the Adder and the Digit Resolver. Tvo nuoibers to be added are presented
each as a set of forty voltages, Ov representing and -kOv representing
1, as Inputs to the forty stages of the Adder. The Adder contains an
analogue feature, in that voltages are added, in part, by the addition
of currents in

<!-- p. 75 -->
63o
a resletor. The output of each stage of the Adder Is one of four possible
voltages^ corresponding to the four possible cases, in which the result of
an addition is a or a 1 with or without carry into the next colvum. The
Digit Besolver is designed to discriminate between these four possible out-
puts, and to give as its output one of two different voltages, which are
interpreted as or a 1.
—
Each stage of the Adder has three inputs two representing digits
of the nuniber to be added, and one the carry from the stage which adds digits
of the next lower coluan of the binary nunbers to be added, and two outputs,
one representing a carry to the next hi^er stage, the other being the one
which the Digit Resolver must interpret as the appropriate digit of the sum.
The physical layout of the Adder closely resembles that of the Regis-
ters. The Adder thus consists of four chassis, each containing ten columns
of four tubes each, one for each digit coluan of a forty binary digit number.
The inputs are taken from B (Resident digit) and from R^ (Incident digit).
In DWG No. 133k will be found a schematic of one of the chassis, the other
four being identical: only the first two and the last two columns of the
chassis are shown in the drawing, as the rest are merely repetitions. It
should be noticed that the left column of the extreme left chassis operates
—
upon the lowest order digits of the numbers to be added that is, upon
the digits in the column 2"^^ -- and the order Increases as we go to the
right.
Consider the first two columns, which will be numbered n and n+1, in
the Adder: reference should be made to the schematic, EWO No. 133^* ^or
simplicity in reference, the tubes of column n will be labelled T^ ^, T^ ^,
T 3,n' . T k,n , while those of column n+1 will be T. ^>^^^ ,, etc. The inputs are:

<!-- p. 76 -->
from R1 (Resident digit) to grids 6 of T2,n and T2,n+1; from R3 (Incident
digit) to cathodes 8 and 2 of T3,n+1; carry from column n-1 to grid 6 of
T4,n, and carry from the n-th column to grid 6 of T4,n+1. Thus tubes T1,n,
T2,n, T4,n, and the left halves of T3,n and T3,n+1 perform the addition in
the n-th column while T1,n+1, T2,n+1, T4,n+1 and the right halves of T3,n
and T3,n+1 perform that in the n+1-th column. The following names for the
tubes are descriptive of their functions: T1,n - "carry gate"; T2,n -
"resident digit gate"; T3,n - "summing resistor driver"; T3,n+1 - "incident
digit gate"; T4,n - "summing resistor driver driver".

In the interests of clarity we will consider the possible cases, and
observe the action of the circuit in each case. These cases are:

| | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) |
|---|---|---|---|---|---|---|---|---|
| Resident digit | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| Incident digit | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| Carry from next lower stage | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| Sum | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Carry to next stage | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 |

First consider case (1). Here the Incident and Resident digits (i.e.,
inputs to cathode 8 of T3,n+1 and to grid 6 of T2,n) are both 0v, and we can
consider the carry digit connection as cut -- it will appear as we go on that
this is correct, as no current flows through this wire except when there is a
carry from the preceding column. Under these conditions the cathode of the
Summing Resistor Driver Driver is slightly above +211v. Hence the cathode
of the left half of the Summing Resistor Driver is slightly higher than this,

<!-- p. 77 -->
65.
so that the voltage at the grid of the Summing Besistor Driver, which is
directly connected to this cathode is 215v. Furthermore, the left half of
the Resident digit gate will be in a conducting stage, so that by cathode fol-
lower action the cathode will be nominally at the grid potential, or Ov, and
the right half will, therefore, be cut off, since its grid is maintained at
-9v. The left half of the Incident digit gate will also be cut off, since
its grid is at -9v and its cathode at Ov. Thus no current will be drawn
through the Summing Besistor (connected between the Sunpolng Point and the cath-
ode of the Siumning Besistor Driver) by either of these gate tubes. The cath-
ode of the ceurry gate will follow the more positive grid and, therefore, rise
to 21^v, so that the left half of this tube will be in a conducting state and
the right half cut off. Hence the voltage at point S will be +215v, as no cur-
rent flows through the Summing Besistor, and no current flows through the carry
connection to the next stage, showing the correctness of our original assumption.
In cases (3) and (5), we still consider the c«u:ry into the n-th stage
as disconnected. In case (2) the Incident digit input drops to -UOv, which
permits conduction by the Incident digit gate; the cathode of this tube will,
of coxurse, only drop to slightly above -9v. Thus the plate current drawn
will be very nearly I65/32 ma = 5.I5 ma, which flowing through the Summing
Resistor will cause a drop in voltage across this resistor of very sli^tly
more than ^k volts. As the right half of the Besident digit gate is cut off,
the output voltage to the Digit Besolver is +l6lv. In case {k), the Incident
digit gate is cut off, but the right half of the Resident digit gate is now
conducting; again the plate current of I65/32 ma causes a drop of 5*^ volts in
the Summing Besistor, so that the output voltage is again +l6lv. In both
cases (2) and (k) we see that the left grid (6) of the carry gate tube (T l,n)

<!-- p. 78 -->
6d»
being at +157v^ tha cathode of thle tube will be slightly more positive, euid
the right half will remain cut off. Thus we have shown that the condition of
"no carry" implies that no current will flow throu^ the "carry" coniiection
to the next stags, which is the assumption that has been used all along in
the analysis.
It has now been shown that if the Incident or Besident digit is a 1,
the circuit will cause the corresponding ^te to draw ^.1^ ma through the
SuoBlng Beslstor. Hence in case (7) a total of 10.3 na. will flow throu^
this resistor, and the output voltage to the Digit Besolver will drop to
-flOTv. Thus grid 6 of the caxrj ^te will drop below grid 5, which neans
that the rie^t half section of this tube will now conduct, tha cathode will
rise to slif^tly more than •»-136v, the left section will be cut off and the
right section will draw very nearly k36/90 = It-.85 ma. This state, which
indicates a carry into the next stage, causes the grid of T]. . to drop to
approximately +12^.
How consider case (2). Here grid 6 of the Summing Besistor Driver
Driver is held at +12Uv; the diode-connected right half has its plate
(12^^ )
maintained at -»-l6lv; hence this section will conduct, and the cathode volt-
age will rise to slightly below t-l6lv. This will, therefore, fix the volt-
age of the cathode of the Summing Besistor Driver. (At sli^tly below this
level; there is, however, a slight rise in voltage from grid to cathode of
the Summing Besistor Driver, so that the voltage at this point turns out to
be very close to -i-lSlv.) Since no current is drawn throu^ the Summing Besis-
tor, the Summing Point voltage (Vg) is +I6lv. This is also sufficient to
raise the cathode of the carry gate to -t-l6lv, and to keep the ri^t half of
this tube in a non-conducting state.

<!-- p. 79 -->
The remaining cases can now be discussed. In cases (4) and (6) the
action of the carry from the preceding stage is to lower the cathode voltage
of the Summing Resistor Driver to +161v, while the effect of the Incident or
Resident one, as the case may be, is to cause a voltage drop of 54 volts
across the Summing Resistor. Thus the output Vs = 161 - 54 = 107v. Hence
the right half of the carry gate will conduct, and so a carry will be in-
dicated to the next stage.

Only case (8) now remains. Here the Summing Resistor Driver cathode
voltage is +161v because of the carry from the preceding stage, while the
current drawn by the Incident and Resident gates through the Summing Resis-
tor causes a drop of 108 volts across the Summing Resistor, so that
Vs = 161 - 108 = 53v.

To sum up, there are four possible results to the addition in the
n-th column: the table gives these, and the corresponding Vs.

| Sum | Carry | Vs | Vs (average measured values) |
|---|---|---|---|
| 0 | 0 | 215 volts | 215.3 volts |
| 1 | 0 | 161 volts | 161.0 volts |
| 0 | 1 | 108 volts | 108.4 volts |
| 1 | 1 | 53 volts | 55.9 volts |

It is now necessary to provide a means by which these output voltages
are interpreted; the result of this interpretation must be that Vs = 215 or
108v ultimately set a toggle in the 0 position, while Vs = 161 or 53v set it
in the 1 position. We need not worry about carries, as we have seen that
these are all automatically taken care of in the Adder. The task of interpre-
tation is assigned to the Digit Resolver, which will now be described.

<!-- p. 80 -->
M.
Physically the Digit Resolver consists of four chassis similar to
those \i8ed in the Adder and located directly above them. Each column of
tubes in the Digit Besolver is assigned to intez*pret the output of one col-
umn of tubes in the Adder. Thus the columnof tubes in the Digit Besolver
are independent of each other, accepting a single input (V from the Adder,
)
and giving a single output to B . A schematic of a single column of tubes
In the Digit Besolver is shovn in IMG No. C-3-1107. For convenience these
will be labelled T,, ..., Tj^ in order from the top downward.
We shall consider in order the four possible cases. First let V- =
+215v, which being applied to grid 5 of T^ causes the cathode to rise
slij^tly higher, thus cutting off the right section of T and the left sec-
tion of Tj^. Furthermore, the cathode of T is raised above +215v, cutting
off the right section of that tube. Now consider T^. If the plate and
grid of the left section were disconnected, grid 3 would assume a potential
of approximately +l63v. Actually, of covirse, grid current flows, so that
the grid is only slightly positive with respect to the cathode. Plate cur-
rent amounts to about k ma which is more than sufficient to hold grid 7
below cut off. Thus the output voltage is determined by the voltage divider
consisting of the k3,l£K., 128.7K, and I88.IK resistors to be +32v.
In the second case, V => -t-l6lv. This is dbill sufficient to hold the
s
right sectico. of T in a non-conducting state, but not enough to do the
same for the left section of T]^, which accordingly conducts, while the ri^t
section is cut off. Again the voltage of grid 6 of T. (+l6lv) is more
than enough to assiore that the right section is cut off. As the left sec-
tion of T. draws approximately 1^88/139 ^3-5 Jna> the voltage of grid 3 of
T falls to about +66v, and the left section of the tube is, therefore, cut

<!-- p. 81 -->
69.
off. The voltage of grid 7 of T would now becOTie +ll6v but for the flow of
grid current, which holds it down to but little above +82v (the voltage of
cathode 8), and the output voltage falls to about -58v.
In the third case, V = +108v. Again the left sections of T^ and Ti^
conduct, while the right sections are cut off. Hence as in the second case
the grid voltage of the left section of T is well below cut off. However,
the voltage of grid 6 of T. is now but sli^tly above +108v, while that of
grid 5 is +136v: the cathode follows the more positive grid, the left sec-
tion is cut off, and the right section draws a plate current of very nearly
k wbl. As in the first case, this holds the voltage of grid 7 of T safely
below cut off, and again the output voltage is approxiaately +32v.
Finally, in the fourth case V •=> +56v ( to use the average measured
value). Hence in T the right section conducts, while the left section is
cut off. The rigiht section of T^ and the left section of T are cut off,
while the other sections conduct, emd consequently, as in the third case,
both sections of T are cut off. Now, however, the plate current drawn by
the right section of T through the 1+3'165 resistor causes the output volt-
age to fall to about -kOv.
To sum up, the Digit Resolver output is +32v in both cases where the
sum digit is 0, while it is far negative in both cases where the sum digit is
1. These voltages are actually considerably larger than needed to operate
the RI Green gates. Hence a diode "burner" is provided at the output of each
stage: the circuit is shown in DWG No. 1288. In stages 2° to 2~^^ , the diode
cathodes are returned to ground, while in the remaining steiges they are re-
txrmed to ground except during the read-in of information from the Input.
Thus during ordinary operation, the Digit Besolver output never swings above
Ov, while the negfttlve excursion Is not limited.

<!-- p. 82 -->

![Fig. 14 — Williams Memory Block Diagram](images/fig_14.jpg)
*Fig. 14 — Williams Memory Block Diagram*

<!-- p. 83 -->

![Fig. 15 — Dot / Double-dot (dash) charge distributions](images/fig_15.jpg)
*Fig. 15 — Dot / Double-dot (dash) charge distributions*

71.
IT . THB WILLIAMS MBOBI
WILLIAMS MBMDBT BLOCK DIAGRAM
There Is no need to enter Into a dlsciisslon of the physical processes
that occur In a cathode ray tube used as a storage derlce In the vay first
C
proposed by F. Williams, as this has been done eLsevhere. We will de-
scribe hov cathode ray tubes are incorporated in electronic circuits In order
to produce a complete memory organ. In the Interests of clarity, ve will
first discuss the functions idilch the circuits are required to perform: from
this a block diagram can be constiructed. When the main features of the memory
organ have been thua presented, it will be time to describe in detail the ac-
tual circuits, and to shov hov the required functions are perfonasd.
The memory organ of the present machine is of parallel type, holding
102l^ bits per tube in a sqviare array, so that kO tubes store 102U forty bi-
nary digit numbers, one binary digit of each number being held in each tube.
A alight modification of the "dot-dash" scheme of storing O's and I's is used,
in that a "dash" here signifies tvo "dots" written so closely together that
the charge distribution produced by the writing of the first of the pair is
considerably modified by that produced by writing the second. Thus we may
suppose that the charge distributions are qvialltatiyely as follows:
+
Dot (0) Double Dot or Dash (1)
Fig. 15.
This picture needs to be Icept in mind while we consider the writing process.

<!-- p. 84 -->
TE.
To write a dot, ve must first generate the deflection yoltagea which guaran-
tee that the beam will be directed to the desired location and then turn on
the electron beam for a short tine. In writing a dash, we must do more:
first a dot must be written, then, after the electron beeuo has been turned
off, the beam position must be moved slightly to one side ("twitched"), then
the electron beam must be turned on again for a short time. Thus we have
for each memory^^catlon two positions: One for the first peak of charge, a
second for the second peak of charge; these will be referred to for convexil-
ence as the A and B positions.
In either writing new Information or In regenerating what already ex-
ists. It Is cleeir that logically we need be able to make only a choice
between the two states of charge that are used to represent I's and O's, emd
hence between two routines for turning on the electron beam. However, the
physical processes of writing a dash where a dot exists, or a dot where a
dash exists, are certainly somewhat different from those of merely "re-
storing" a dot or a dash. Consider the writing of a dot on a dot: we merely
have to build up the charge In the A position to Its equilibrium position.
On the other hand. If a dash already exists and we wish to write a dot over
It, It Is clearly desirable to leave the beam on In the A position for a
longer time, so that more secondary electrons will be permitted to return
to the screen to nullify the concentration of positive charge In the B posi-
tion.
If a dash Is to be written where a dash already exists. It Is clearly
sufficient to turn on the beam In the A position only very briefly, while In
the B position It must stay on long enough to bring the charge up to the
equilibrium value. On the other hand. In writing a dash over a dot. It Is

<!-- p. 85 -->

![Fig. 16 — Beam turn-on timing for the four write/read routines](images/fig_16.jpg)
*Fig. 16 — Beam turn-on timing for the four write/read routines*

desirable to leave the beam on In the B position aooevhat longer, in order
that more secondary electrons will be available to return to the screen and
nullify in part the accusmlation of positive charge in the A position. Thus
ve are led to distinguish four possible routines:
(1) Write a dot where a dot exists ("normal dot") (TT)
(2) Write 'a dot where a dash exists ("superdot") (HT)
(3) Write a dash where a dash exists ("normal dash") (HE)
(k) Write a dash where a dot exists ("superdaah") (TH)
In the brief designations of these four processes (TT, etc.)» the letters T
and E are the last letters of dot and daah, the first position signifies the
existing state before the writing process, while the second signifies the
state to be created. In all cases the beam is turned on in positioci A in
order to sense what information is stored in the location in question: this
is obviously necessary in the reading or the regeneration process, ^ile in
the writing process, It is necessary to compare this Information with that
which is to be written, and thus to select which of the four routines TT,
ET, EE, IS is appropriate. The following timing diagram for the turning on
of the electron beam is useful.
' 1 1
M
1

<!-- p. 86 -->
J%.
In all cases the electron beam is turned on at t , vhlle between t auad t .
1* 5
a period diirlng which in all cases the beam Is tvimed off, the "twitch" takes
l>lace; thus in t.t, the beam Is directed toward the A position, while in the
t^t It Is Inthe B position. We note that in the Normal Dash routine the
beam is on in the A position for a shorter time than it is in the Superdash
routine: hare an autooatic turn-off of the beam occvirs, which will be ex-
plained when ve describe the operation of the Discriminator circuitry. '
We have seen what beam-tum-on routines are needed for performing
the read-regenerate and the write functions. To carry out these routines,
properly timed sequences of pulses are needed in each case. Hence it is nec-
essary to provide not only these pulses, but also means of selecting the
required sequence, means of "reading" what is stored in any given memory loca-
tion, and meeins of deflecting the cathode ray tube beam to the desired memory
location. Furthermore, since the contents of the memory must be periodically
regenerated, it is clear that a fundamental repetition rate must be provided.
In the following discussion we shall illustrate, with reference to
the block diagram, hcv the functions outlined above are accoopllshed. It is
simplest to start with the cathode ray tvibe-amplifier-discrimlnator loop.
It should be noted that each of the forty CST's in the memozy organ has its
own output Amplifier and Discriminator; all the equipment represented by
other blockd in the diagram is ccsmon to the forty CRT's. At the beginning
of each read-regenerate or write cycle the Discriminator tvims on the electron
beam In the GtT by red.slng the potential of the control grid. The Amplifier
merely raises the CRT output signal to the required level, which calls for a
gain of about 2 x 10^, its output being used to set to or 1 a toggle in the
Discriminator, which has previously been cleared to 0. The Discriminator Inputs

<!-- p. 87 -->
n*
are. In addition to that from the Amplifier: (I) pulses to clear the toggle
—
and initiate the beam txim on routine these are the saoe no matter what
routine is performed; (2) four pulse trains 80^^, SA^^, SOg, SA^ which differ
according as reading, regenerating, or vriting Is required; (3) the digit to
be mritten frcn B., this being via a gate which is enabled onl7 when writing
is called for. In eiddltlon to the beam-tum-on output, there is one from the
Discriminator toggle to BUI, which is rla a gate enabled only when reading
is required.
A block labelled "Timing Pulses" appears in the diagram. Physically
this contains a "Memory Clock" which provides the basic repetition rate, and
ium "Pulsers" which generate pulses beginning at various times in the cycle:
tl^se pulses are of different lengths as required, and each is isBBediately
followed by a standard "termination" pulse. These are: Inspect, IT, HT,
Twitch Delay (TD), HE, IE, and three others; A, CI, and B, which are needed
to step the Dispatch Covmter in the Main Control. Termination pulses cure
designated by a small "t" subscript: as SD , etc. The time sequence is 11-
lustrated in Fig. VJ, where the "termination" pulses are omitted. The clock
pxilse' Is also used to clear the Discriminator toggle to 0, and so is usually
designated by t>e abbreviation "CI T ".
It has.been xymarked that it is necessary to provide the Discriminator
with four trains of pulses, SO^^, SA., SO , SA to enable it to carry out the
read-regenerate-process, emd a different set of four trains to carry out the
write process. These trains are fomed from tietiming pulses Just discussed
in the block labelled "Discriminator Pulse Boutlne Generator"; it will be
noticed that there is an input to this block labelled "Bead/Vrite" : this
signal determines which set of pulse trains SO., ..., SA^ will be transmitted

<!-- p. 88 -->

![Fig. 17 — Discriminator Pulse Routine Generator timing](images/fig_17.jpg)
*Fig. 17 — Discriminator Pulse Routine Generator timing*

n^
to the Dlscrlalnatar.
»>:•
Clock (CI T^) _rLJ!!!lJ n_
^
Settling Delay (SD)
Inspect (I) -TL
TT
HT
TD
HE
TH
JT
A
CI ji_
B J~L
Fig. 17.
The Bead/tfrlte Input to the Dlacrliiilnator Pulae Boutine Generator cooes
from the block labelled "Local Control". Here signals are received frcn the
Main Control (not, of course, a peurt of the Memory), and frca the Tladng Pulse
Oenerator. The signals frcn Main Control signify: (1) "T^b/TSo" - the Meaory
is to be used or not; (2) "Bead^rite" - a read-regenerate or a-vrlte routine
is called for. Local Control transmits the Bead/^frite signal to the Discrln-
inator Pulse Boutine, and also actuates the electronic switch vhich determines
whether the address standing in the Dispatch Counter or that standing In B. is
to be transmitted to the Deflection Oenerator. Local Control also transmits
back to Main Control the following signals: Ackncwledge "Tes", Clear BUI,
Oate BUI, Finish, whose significance will be made clear when we undertake

<!-- p. 89 -->
.
n.
the detailed description of the Local Control.
Finally, the Deflection Generator merely receives as inputs the co-
ordinates of the Memory location to which the CRT electron beam is to be
directed and generates the appropriate deflection potentials. The "twitch"
generator's function is obvious: it is actually part of the Deflection
Generator, but its action Is initiated by the ET (superdot) termination
pulse
MEMORT CLOCK
The necessity of periodically regenerating the information stored in
the Williams Memory makes it necessary to provide a timing device. In the
present machine, this is called the "Memory Clock".
As there is nothing in the operation of the Memory that requires the
maintenance of a very precise repetition rate, and as it is desired to per-
mit the rate to be varied over a rather wide range (from U^kc to l43kc in the
present model), for convenience in testing it is entirely feasible to use a
multivibrator as the fundamental rate-determining circuit. The output of
the multivibrator is used merely to ring a peirallel LC circuit, the natural
period of which determines the pulse duration.
The Memory Clock schematic is given in DWG No. 1217' The multivi-
brator appears at the left of the drawing, (tube B (a 6j6) and. its associated
components). The diode A is added to sharpen the plate voltage recovery.
The plate voltage of the conducting half of the 6J6 falls to about 30v; when
this section of the tube is cut off, its plate voltage begins to rise expo-
nentially toward 300v; and hence is rising quite steeply when it reaches 150v,
where it is stopped by the diode. Hence, the multivibrator output resembles
waveform I in Fig. l8. The fall in plate voltage is quite abrupt; this sharp

<!-- p. 90 -->

![Fig. 18 — Memory Clock waveforms](images/fig_18.jpg)
*Fig. 18 — Memory Clock waveforms*

<!-- p. 91 -->
79.
present p.r.r. la itO KC.
The output from the multivibrator is taken from the plate of the
right-hand section, and applied to grid of the left-hand section of tube D
(a 6j6). The coupling network time constant is .001 sec, which id suffi-
ciently larger than the longest period available so that no serious distor-
tion results, while the left-hand half of the diode C merely clamps the top
of waveform I to ground. Thus the input to tube D is again waveform I, but
now the swing is from Ov to -120v.
Now consider tube D. Its right-hand grid is maintained at -lOv, so
that during that part of the cycle when the left-hand grid is at groxuad
potential, the left half is in a conducting state, drawing plate ciirrent
through the 2'h mh inductance; the cathode will be slightly above ground
potential and the right half consequently cut off. At time t the left
,
grid suddenly falls to about -120v, so that the left half will be cut off,
and the current transferred to the right half.
Thus the initial conditions for the circuit formed by the inductance
in parallel with its distributed capacity are: current flowing in the coil,
and a slight charge in the capacitance. The parallel LC circuit will, there-
fore, begin to oscillate. The voltage across the coil will start at close
to (actually a volt or two, due to the non-0 resistance of the coil), and
will so swing that the voltage of the end of the coil not attached to the
+100v bus will go positive with respect to +100v; this ezcxirsion of amplitude
approximately 50 volts, will, of course, be sinusoidal, at the natural fre-
quency of the LC circuit (which is very close to ^ mcps). When, however, the
first half period has ended, and the end of the coil not attached to the bus
begins to swing negative with respect to the bus, the right half of diode C

<!-- p. 92 -->
.
80.
vlll begin to conduct: this, togsether with the J^^.TTt resistor critically damps
the LC circuit, so that at each fall of volta^^ at the right-hand plate of the
multivibrator, a single positive half sine wave is transmitted to the grids
of tube F. The d.c. level from which this owing starts is clamped to Ov by
the left section of diode E. The signal applied to the grids of tube F is,
therefoire, as shown in waveform II. The internal t t^ is very nearly one
microsecond, and this is clearly independent of the repetition rate of the
multivibrator
Tubes F and G are both 6j6's each being so connected that it acts as
a single tube. The grids of G are maintained at +10v, so that, as long as the
grids of F are held at ground potential, the cathodes of both tubes, vhlch
are connected together, are held at sll^tly above +10v, with the consequence
that F is cut off. How in the interval tpt-, during which the grids of F are
driven to approximately +50v, tube F is caused to conduct so that its cathode
follows the grid so hi^ that G is in turn cut off: this causes the plate
voltage of G to rise sharply from about 50v to lOOv; of course, it will fall
sharply by a like amoxmt when current switches from G back to F again shortly
before t^ . Thus the plate voltagp of tube G is as shown in waveform III.
We now have to consider only the output cathode follower, tube H. With
the left-hand grid held at -lOv, and the ri^t at -25v, a condition which per-
sists except in the intervals t t,, the left half will conduct, the right half
will remain cut off, and the cathode potential will remain at very little
above -lOv -- which is the output voltage from the Memory Clock in these in-
tervals. When now in intervals t-t- a 50v pulse is emitted by tube G, the
voltage of the ri^t-hand grid of G will rise to +10v, where it will be caught
by the rij^t half of diode E; consequently, the cathode of H will rise to

<!-- p. 93 -->
. "
61.
vary sllj^tly above +10v during tinie intervals t t^, which gives us the out-
put waveform IV.
WILLIAMS TQBE FOLSERS
The operation of the ViUiaas Memory requires the availability of a
niuiber of pulses occurring at definite times in the cycle of the Memory
Clock (see 71g. 17) • The circuits used to provide these are called "Pulsars
They eure all designed to accept as Inputs pulses of essentially rectangular
shape, rising from -10 to +10v, and of duration .5 ^s or greater. The
pulser output consists of two pulses. The first is one whose length may be
varied; the leading edge of this pulse occurs at the same time as that of
—
the input pulse. The second Is in all cases of fixed diuration approxi-
—
mately *^ us with its leading edge sjmchronized with the trailing edge of
the first pulse. The second ptilae output is of about half the duration and
of the same amplitude as that of the Memory Clock, and can be (and is) used
as an input trigger to other pvilsers. Both time durations are established
as one half the period of a parallel LC circuit. In the case of the first
pulse, variation of the valxies of Inductance and capacitance permit vari-
ation of pulse duration over a fairly wide range. A table is given in
TfHQ Ho. 1216 i^lch shows the ranges of pulse duration available in the
pulsers of the present machine.
Let us ncfv consider the< operation of the circuit (see EWG No. 12l6)
Between pulaee the rig^t-hand grid of tube A is held at -20v and the left-
hand grid at -lOv. Under these circumstances, the cathode of A is sli^tly
above -lOv, ths rl^t half of A is cut off, and in tube B, the left- and
ri^t-hand grids of which are at -lOv and ground, respectively, only the
ri^t half is in a conducting state, plate current of approximately U.2 ma

<!-- p. 94 -->
being dravn through the 1 mh inductance. We aiBsuiBe that no transient oecll-
lation is present In either LC circuit: the fact that each LC circuit has
connected across it a diode (consisting of the cathode aid.one grid of tube C)
and resistance chosen at the critical damping value of the circuit assures ua
that no transient will persist essentially beyond one period. Thus both
plates of B are very nearly at +I5OV (the left grid will be at this voltage,
while the right one will be very slightly below because of the non-0 resist-
ance of the 1 mh inductance). Thus the cathode and both grids of tube C are
at -fl^Ov, so that both secticns sire in a conducting state; the plate poten-
tials turn out to be about +225v. Clearly diodes D and E are now conducting,
while only the rlg^t half of tiibe ? is conducting, the cathode^ therefore,
being sligjitly above -lOv.
With the arrival of the Input pulse at the left grid of tube A, the
cathode will follow the grid to slightly above this voltage: we note that
this is also automatically the leading edge of the "Pulse Out", which is,
therefore, not delayed with respect to the Input pulse.
The left-hand grid of tube B is now driven to slightly above +10v, and
the cathode follows it, thus cutting off the rig^t-hand section. This abnzpt
switch, of course, sets up transient oscillations In the i>arallel LC circuits
in the plate leads of tube B. The right-hand plate swings positive with re-
spect to -i-l^Ov. Thus the left-hand grid of tube C becomss positive with
respect to the cathode; and grid current flows through the 2.2E resistor in
series with the grid: the value of this resistor Is chosen so as to assure
that the parallel RLC circuit consisting of the Inductemce and capacitance,
the grld-to-cathode resistance of the left section of C, and the 2.2K resistor
is critically damped. Of course, the plate current of the left section of C

<!-- p. 95 -->
83-
Is Increased somewhat emd the plate voltage decreased; this change Is trans-
mitted to the left grid of tube J , which has already been shown to be below '
cut-off. Hence this transient has no effect on the output of the Pulser. On
the other hand, the transient set up in the plate circuit of the left section
of B is such that the plate swings negative with respect to +150v: the exact
amount of this swing, of course, depends on the square root of L/C; for all
the values used it is never less than about 28v. The right section of C cuts
off when the grid is about six volts below the cathode, a level which is
reached in at the most 7% of the half period of the LC circuit. The plate
voltage is not, however, permitted to rise all the way to +300v; it is
"caught" at +260v by the Left section of diode D, -a level \rtxich will obvi-
ously be reached considerably before the grid voltage reaches cut-off, so
that the rise from f22^ to t-260v is accomplished in a little over JjL of the
half-period of the LC circuit: at the end of the half-period, of course, a
fall of lilEe amount takes place. Thus a pxilse of about 3^v amplitude is
C
created at the ri^t-hand plate of The ri^t-hand plate of the 30 upf
condenser is maintained at -20v before the pulse begins, so that since the
i cathode of diode E is held at -flOv, at this point a pulse rising from -20
to +10v appears: these levels are accurately defined, and it is apparent
that the exact magnitude of the pulse at the right plate of C is unimportant
provided it exceeds 30v. A similar remark applies to the magnitude of the
negative swing of the rig^t grid, of C: it needs only to be sufficient to
raise the plate voltage to +26O7 in a time short compared to the half-
period of the LC circuit. The pulse produced is applied to the right-hand
grid of tube A, which rises to +10v. Thus though the input pulse to the left
grid of A shortly drops from +10 to -lOv, the cathode is held at ali^tly

<!-- p. 96 -->
8H,
above +10v for a time determined by the half period of the LC clrciilt.
At the end of the negative sving of the right-hand gyid of C, the
voltage of the rig^t-hand grid of A falls again to -20v; the cathode, how-
ever, is "caught" at -10: this fall marks the end of the "Pulse Out."
This fall also causes a svitch in current in tube B: the right-hand half
once more is caused to conduct, and the left is cut off. We must once
more examine the behavior of the LC circuits in the plate leads.
It is nov time for the second half cycle of the oscillation of the
circuit in the left plate lead. However, when the lower end of this starts
to go positive with respect to the upper end, the rig^t section of C begins
to draw plate current, and its grid to cathode resistance, in addition to
the 2.7K resistor, critically damps the oscillation. The drop of the plate
voltage of this section below +225v drives the ri^t-hand grid of A below
-20v, but this cleeurly has no effect upon the cathode voltage of A, and
hence the "Pulse Out" voltage, •irtiich remains at sli^tly above -lOv.
However, the 1 soih inductance — 20 y^ condenser combination now jaro-
duces a trajssient: the end connected to the ri^t-band plate of B swings
negative with respect to +I5OV throiigh a half period of a sine wave of
about 28v amplitude. This drives the left half of C below cut-off; the
plate voltage begins to rise toward +300v, but is caught at +260v by the
left section of diode D, and we get a pulse of approximately 35^ amplitude
^
lasting for nearly .5 at this point. Note that in determining the period
of oscillation it is necessary to take into account, in addition to the 20 yiyf
condenser, any distributed capacity that is present -- this is of sufficient
smgnitude to make the resonant frequency close to 1 mcps. Diode S limits the
rise of grid voltage of the left section of F, so that this point rises from

<!-- p. 97 -->
85.
-20v to +10v during the pvilse, and hence the cathode rises from slightly
above -lOv to slightly above +10v for very nearly .5^. This is the
"Pulse Bnd" pulse: as we said before, its leading edge is determined by the
termination of the Pulse Out pulse. As the 1 mc oscillation attempts to
enter its second half cycle, the left half of C draws grid current, and
critical daBQ>ing agialn ensiivs. Thus the circuit is returned to its quies-
cent state, awaiting the arrival of the nextftinput pulse.
There are ten pulsers of the kind Just described. One of these, the
"Settling Delay" pulser. Is triggered by the Clock pulses; its pulse output
is not used, but its terminaticQ pulse triggers the Inspect, TT emd HT
pulses. The termination of the HT pxilser triggers the TD pulser, and its
termination pulse triggers both the TH and EH pulsers. The TH termination
pulse triggers the A pulses, its termination pulse the CI pulser, and finally
Its termination pulse the B pulser. A pulse called the "Strobe" is used in
the Discriminator: it is an inverted and slightly amplified version of I,
dropping from to about -kftw for the duration of I. It is generated by a
circuit located in the sane chassis that contains the Local Control and the
Pulse Eout1^ Generator and will be described with them.
Fig. 19 shows the actual waveforms observed, together with the timing
actually used in the computer. We will see later how various of these pulses
are ccobined to give the Discriminator Pulse Routine voltages used in the
Discriminator. We also note that the I pulse is not used directly, but is
first passed through an amplifier and d.c. restorer to produce the negative-
going pulse actually used in the Discriminator. The actual voltage levels
eniployed are shown In Fig. 19: these are very close to the "nominal" values
of -lOv emd +10v which we used in the discussion of the pxilser circuit:

<!-- p. 98 -->

![Figure 19 — Pulse durations (in microseconds)](images/fig_19.jpg)
*Figure 19 — Pulse durations (in microseconds)*

£
86.
JVXl
CLCCk:
y/2
SD
TT
-A
/.5-r
HZ
\
-^2.2.
NT
2.6 .J
TD
-^
1.1
t/2.S
UN -IPS-
4.25- *-i
I t
TH
^,75' .-Ir z
\
rrz
CL
Ui J
moderate deviatlona front the nf*'^'' values have no effect on the operation
of the circviits to vhlch the pulser outputs are applied.
The termination pulses eo-e not shown. Hcwever, these all rise at the

<!-- p. 99 -->
87.
termination of each pulse and laat for approximately .5 jua. They are
designated by the letter that describes the pulse at whose termination
they rise with a aaall "t" subscript, aa for example I , TD , etc.
THE WILLIA>B TDBE OUTPUT AMPLIFIKE
The current that flows to or from ground to the cathode ray tube
pickup screen during a reading operation Is very feeble. A resistor being
Inserted between these points, the resulting voltage must be amplified to
bring the output up to the desired voltage level. Thus each cathode ray
tube in the Williams Memory is provided with an amplifier, the schematic
of which appeeo-s in DWG Ho. 1367- The physical structure of the ampli-
fier is of annular form: it is mounted within the shield that encloses
the cathode ray tube, directly in front of the tube, which minimlzea the
length of the lead from the pickup screen to the grid of the first tube
of the amplifier.
The input resistor was chosen aa 100,000 ohms, which meana that
the maximum amplitude of input voltages are approximately .25 mv and 1 mv
when a or a 1, respectively, is read. A gain of 30,000 provides output
signals of maximum amplitude 7 ««id 30v, respectively, which are ample for
the purpose for which they are used in the Discriminator.
It was desired to hold to a low value any 60 cycle hum due to
cathode leakage and modulation of the electron stream. Given the chosen
value of grid-leak resistance, the value of 1000 uuf for coupling la
chosen to guarantee that the gain at 60 cps is less than unity. As the
tubes are to be operated at not over half the rated plate and screen
dlsBipatlon, the plate decoupling resistor and the screen grid resistor

<!-- p. 100 -->

![Fig. 20 — Discriminator output signals](images/fig_20.jpg)
*Fig. 20 — Discriminator output signals*

<!-- p. 101 -->
The Discriminator distinguishes between these two: it contains a toggle
which is set by the euaplifler output to the state corresponding to the bit
of InTormatlon read. The Discriminator is furthermore supplied with four
trains of pulses frcan the block in Fig. ik labelled "Discriminator Pulse
Boutine Generator"^ which are of one configuration if reading or regenerat-
ing is called for, but of a second configuration if new information is to
be written over that presently in existence. If reading or regeneration
takes place, the Discriminator causes the electron beam of the cathode ray
tube to be turned on the required time (Normal Dot or Normal Da^h) to re-
store the existing state of charge, while if writing is to be accomplished,
the circuitry ccmpea*es the existing bit of information with that which is
to replace it, and turns on the electron beam in the Nonnal Dot or Normal
Dash routine if the new Information is the sajne as the present, or in the
Superdot or Superdaeh routine in case a is to replace a 1, or vice versa.
We will now describe the operation of the Discriminator, referring
to DWG No. 12hl.
The lower row of tubes in the drawing consists of one toggle ("T ")
and associated gates, used to present information to the toggle and to ex-
tract information from it. This toggle is the first element of the circuit
affected in each cycle of the Memory: at the time of each Clock pulse, it
is cleared to 0, i.e., to the state in which the left half of the 6j6 Is
conducting. This is accomplished by a cleeir driver and clear driver-driver
circuit, Just as in the case of the register toggles.
The next operation in the memory fijcle is to tvccn on the electron
beeim of the cathode ray tube to inspect the contents of the pcurticxilar loca-
tion in the memory tube which is currently of interest. In the "read

<!-- p. 102 -->

![Fig. 21 — Digit Resolver input circuit](images/fig_21.jpg)
*Fig. 21 — Digit Resolver input circuit*

<!-- p. 103 -->
,
90.
actually this voltage can vary eia much as 5 volts either way owing to the
resistor tolerance of lOjt wlthovrt causing any difficulty.
The connection to the CRT control grid Is mawle aa shown in the upper
right-hand comer of TWO No. 12*^1. The cathode of the CRT is maintained at
+3l9v, so that If the cathode of the 6AL5 is held at or above +288v, the
CRT grid is held at +288v, and the electron beam is on. Dropping the grid
to +28OV is sufficient to cut the beam off, and clearly this cem be done by
dropping the 6AL5 cathode voltage to sli^tly below this level. The volt-
age of the 6aL5 cathode is determined by the 5687 shown in the upper left-
hand comer of the scheiaatlc. If the rl^t-hand section of this tube draws
no current, the grid of the left section will be at +300v and the cathode
subtly above this value: this is obviously sufficient to hold the 6/U.5
in a non-conducting state and thus permit the CRT electron beeun to stay
"on". On the other hand, if the right-hand section of the 5687 carries a
current of 6 ma, the grid of the left section will drop to +255v: the
cathode will be sli^tly above this, and, therefore, the CRT control grid
will fall safely below the cut-off level. Actually about 3 ma would suf-
fice if all the values of resistors in the circuit were precisely as given
in the schematic, and not subject to tolerances.
It is, therefore, necessary in all cases to assure that no current
Is drawn by any of the gates which read out from T or from To at the begin-
ning of the Inspect pulse.
We shall now establish the waveforms of the pulse trains SO SA.
,
SOp, SAp which are needed.
First consider the "read-regenerate" case. Here SO,, ..., SAg must
be such that the beam turn on corresponds to the "normal" cases, T£ and HH.

<!-- p. 104 -->
91.
There is no reason to consult T , so both gates to which it is connected
must be held In the disabled condition throughout the cycle, which is done
by holding SO at +70v and 3A at +120v. This is sufficient to assure ua
that the left-hand sections of both the T output gates will remain in a
non-conducting condition.
As far as T is concerned, it is definitely known that it initially
contains a 0; hence the left-hand gate, which reads out from the right-hand
grid of the toggle will not conduct if its cathode is held sufficiently
above -35v to assure cut-off, while the right-hand gate will be non-conducting
if its cathode ie1held •uf1ficiontl2y above Ov to assure cut-off. Voltage
levels of -lOv and +10v are convenient and sufficient for this pxirpose.
Thus if SA =« -lOv, SO = +10v, SA = +120v, SO = +75v during the
2
Inspect pulse, we will be assured that the CRT electron beam is turned on
at the beginning of the"pulse time.
During the Inspect time the information stored in the location on
the CRT phosphor to which the beam is directed is made available to the Dla-
criminator as follows: the input to grid 7 of the 12AD7 is held at Ov except
dxiring the Inspect time when it drops for .5 us to -25v (the pulse that ac-
complishes this is called the Strob^. Note that the grids of the 6j6 are
biased to -20v and -lOv, respectively, so that before the Strobe pulse both
Bectlona of the 6j6 are cut off.
During the Strobe we have two possibilities. In case a is read, the
signal from the amplifier rises to +5v during the Inspect period; hence, the
ri^t-hemd grid of the 6j6 rises to -5v, and hence the cathode following it,
the left section remains cut-off, and no signal is tremsmitted to T^^. T^
having been Just previously cleeo-ed to 0, continues to hold a 0. In case a 1

<!-- p. 105 -->
92.
ia read, the amplifier output drops from Ov to -20v during the Inspect pulse,
thus driving the voltage of the right-hand grid of the 6j6 down to -30v. The
cathode voltage drops also, but will be "caught" in the vicinity of -20v as
the left section begins to conduct. The plate current of this section, flow-
ing through the I5K plate resistor of the right-hand section of the toggle
tube flips the toggle to the 1 condition. Thus by the end of the Strobe pulse,
the information held in T is identical with that stored in the CRT location
that is being read.
Now to continue with the read-regenerate case, there aa-e Just two pos-
sibilities: either a or a 1 is stored in the given memory location. If it
is a 0, the toggle T ia not flipped during the Strobe time, and hence the
CRT electron beam will stay on as long as the values of SA , ..», SO ajre
maintained. These must, therefore, be maintained a length of time correapond-
int to the Normal Dot. It is convenient to take the quiescent values as fol-
lows: SA = -lOv, ' S 1 O = -lOv, SA = +120V, SO = +70v. Then for Normal Dot
1 2 2
(TT) SO. rises to +10v at the beginning of the Inspect pulse, and returns to
-lOv at the end of Normal Dot time, which occurs slightly before the end of
the Strobe pulse. The other possibility is that the memory location in ques-
tion holds a 1. Suppose the voltages SA , ..-, SO are as determined above.
Shortly after beam turn-on, the toggle T is flipped. The grid voltage of the
left-hand section of the toggle tube now becomes -35^, while that of the right
section becomes Ov. As SA is -lOv and SO is +10v, right gate is unaffected
while the right-hemd section of the left gate now draws plate current of ap-
proximately 300 A^ * 6.32 ma, vrtiich is more than enough to turn off the CRT
electron beajn. Actually, we would prefer not to turn on the beam at all in
the A position, but clearly this must be done in order to ascertain the state

<!-- p. 106 -->

![Fig. 22 — Discriminator pulse routine voltages (read/regenerate)](images/fig_22.jpg)
*Fig. 22 — Discriminator pulse routine voltages (read/regenerate)*

:
93.
(0 or 1) of the point: it turns out that in the present case the beam la
turned off sufficiently rapidly so that not much charge is huilt up in the
A position. Hence, the pulse distribution voltages SA etc. that suffice
,
for dot regeneration also suffice for the regeneration of the A position of
a dash.
Cle€irly the B position of the dash must also be regenerated after the
twitch. This is done by holding SO at -lOv, but raising SA to +10v for a
time equal to the Normal Dash regeneration time: these voltages are clearly
adequate to disable the T read out gates. We note that in case T holds a
0, these values of SO, and SA, still permit the left section of the right T
Xead out gate to draw 6.82 ma of current, so that in the dot case the beam
will stay off after it has been twitched to the B position.
Hence we have shown that for reading and regenerating both O's and I's
the following modes of variation of the Discriminator pulse routine voltages
suffice
[^
TO
r
SO,
J — -^/O
S£l I 1 I /o
Fig. 22.
During this cycle SO and SA are maintained at +75v and +1^0v, respectively.
We now turn to the write case. Here instead of two possibilities we
have four, which have already been designated as: TT, HT, HH, !EE. Fortunately,
a single set of Discriminator pulse routine voltages suffices: we proceed to

<!-- p. 107 -->
9h.
derive these.
As before, the CRT electron beeua must be turned on in synchronism with
the Inspect pulae* The TT ceise requires, therefore, that SO be raised to
+10v, and maintained at that level during the^ time required for dot restora-
tion (Normal Dot). During this time, the level of SA^ is clearly of no con-
sequence, as either of the possible levels vill keep the left section of the
gate In a non-conducting state. The same is true of SA • SO must be held
at +75v during the Normal Dot time.
Now consider the TH case. As in the TT case, the left grid of the
toggle tube is at Ov and the right at -35v, while the voltage of the T lead
is +110V. The CRT beam must be turned on at the beginning of the Inspect
pulse, turned off at the expiration of the time required to write the A part
of the dash, turned on again at the end of the twitch settling delay, and
turned off again at the expiration of the TH pulse (Superdash). SA must,
therefore, be raised to +120v at the beginning of the Inspect pulse, and
dropped back to +100v at the end of the time required to write the A paxt
of the dash. At the expiration of the twitch settling delay, SO must be
raised to +10v, ajid SA- to +120v to assure beam turn on. One, at least, of
these voltages must be dropped again at the expiration of the time required
for Superdash. We do this to SO SA can be dropped any time before the
;
beginning of the next cycle. The values of SA and SO in this case clearly
are of no importance: all we have so far determined (from the TT case) is
that SOp must be held at +75v during Normal Dot; it certed-nly must be raised
to +100V at the end of TD, and held there at least until the fall of SO^^ for
otherwise no current would be drawn from the summing bus during that interval
and Normal Dot restoration could not be accomplished.

<!-- p. 108 -->

![Fig. 23 — Discriminator pulse routine voltages (continued)](images/fig_23.jpg)
*Fig. 23 — Discriminator pulse routine voltages (continued)*

>5.
Thus, so far we have determined the follovlng waveforms for the
Dlscrlmlnatcr piilae routine voltages:
rj~ TD
i I I
J L 1 I ^7S-
So,
J. , _ _ - ___--_ r/
y
O
o
1 I I —
—^/ec
Fig. 23.
We n<w turn to c&ses HT and HH; in both of these the toggle T is
flipped to the 1 position during the Strobe pulse.
In case HT, the CRT beam must be kept on for Superdot tins, which is
longer than that required for Normal Dot restoration. This can be done by
raising SA fran -lOv to +10v for this period, at the sane time holding SO
at V^v. At the end of this time, either SA must be dropped to -lOv, or
1
SO raised t'o +100v (we actually do both) : Clearly these modes of variation
cause no difficulty in the TT and HH routines.
Finally consider case HE. SO and SO are here Important, while the
vea*iation of SA and SA suffice for the restoration of the A position. We
also raise SA to +10v at the expiration of the twitch settling delay for the
time required for normal restoration of the B position. As noted before
(under TH) SO is raised to +100v during the Superdash interval, so that the
beam is guaranteed to be turned on during the shorter Rormal Dash restora-
tion period.
Thus we have established the waveforms of the Discriminator pulse
routine voltages: Fig. 2^ gives the set for (a) the read-regenerate case.

<!-- p. 109 -->

![Fig. 24 — Pulse routine voltage waveforms, read and write cases](images/fig_24.jpg)
*Fig. 24 — Pulse routine voltage waveforms, read and write cases*

<!-- p. 110 -->

![Fig. 25 — Final pulse routine voltage waveforms](images/fig_25.jpg)
*Fig. 25 — Final pulse routine voltage waveforms*

<!-- p. 111 -->
The circuits uc;ed to develgp the pulae routine voltaj^ea vrtiich we
have been diacusoing are described iii the next L-ection on t!iO Pulse rou-
tine Generator. In Fig. 2^ are shown the actual wavefornn obtained.
PUUJE KOUTINE QENERATOE
We will now show how the outputs of the puleers are combined to
produce the pulae routine voltafjes which were shown to be needed for the
operation of the Discriminator. The circuits are quite straight forward;
a schematic is given in DWGS. No. 0-l'+70 and B-200L.'.
The inputs to the generator are: TT, TH, HT, HH, Clear T, , I, CI, TD,
and two voltai^es one of which is -20v for read-regenerate and +lDv for uTice,
the other +10v for read-regenerate, -20v for write. The outputs are: SA,
,
SO,, 3A,^, and SO^^ to the Discriminator, and the twitch pulse, which rises
from -20v to +I0v with the leading ed^^ of TD, and falls back to -20v with
the leading edge of CI, i;o the Deflection Generator. The twitch pulse is
generated by the toggle labelled "twitch" In the schematic. An output is
taken via a cathode follower to the SAp generator, while the use of the in-
puts CI and TD in triggering the toggle axe clear from the schcraatic
Ve will now consider the generators of SO, , SAj^, SA^, SO^ in order
as they appear In the drawing. Reference is made to Fig* 2l4- where the
desired waveforma are shown.
In the write case, the 6.8k resistor being supplied with +10v and
the diode cathode varying with TH, the left grid of the 6j6 is held at
-lOv except during the TU pulso, when it is raised to +10v. The input to
the rii^t grid of the 6j6 is TT, which stays at -lOv e:^cept during the TT
puldo tiiaa. The ;>667 is, of course, Dierelj/ a cathode follower. Honco the
SO, output is -lOv except during the TT and TH pulses, when It rises to +10v.

<!-- p. 112 -->
9^
During the read-regenerate case, the diode plate is constantly held at -20v,
as TH never falls belov this level, and hence the cathode of the 6j6 fel-
lows the higher grid, which is at all times the right one. Thus, the output
is -lOv except during the TT pulse, when it rises to +10v.
The operation of the SA generator is the same. In the write case
the voltage of the left grid of the 6j6 is -lOv except during HT, when it
rises to +10v, and that of the right grid ia -lOv except during HH, when it
rises to +10v. Hence the output is -lOv except during the HT and HH pulses
when it is +10v. During a read-regenerate cycle the left grid of the 6j6
is constantly held at -20v, so the output follows the variation of HH, being
-lOv except during HH, when it rises to +10v.
In the SA generator we note that the cathodes of the two 6j6'3 to
2
which the inputs are applied are connected together, and that the ri(^t grid
of the right tube is grounded. Thus this section will be cut off if the cath-
ode voltage is above about +5v, under which circumatance the grid voltage of
the 5687 is "bumped" at +120v by the right section of the 6aL5; on the other
hand, if the right section of the right 6j6 conducts, the input to the 5687
is bumped at +100v by the left section of the 6AL5. In the write case, the
right section of the right 6j6 will, therefore, conduct except during I and
the time from the beginning of TD to the beginning of CI when the twitch
voltage rises to +10v. Hence the SA output in the write case is +100v
2
except during I and the time the twitch voltage is +10v, when it rises to
+120v. In the read-regenerate case the right section of the right triode is
constantly non-conducting, so the output is constantly +l20v.
Finally, we have the oOp generator; we note that the inputs are applied
to a 6j6 at the left and to one at the right, which appears just above the

<!-- p. 113 -->
10
.
5687 cathode follower in the schematic. This second 6j6 is sc arranged that
its left section conducts except while the Diocriminator toggle T is being
cleared: thus, the voltage of the right grid of the center 6j6 is held at
Bomewhat below +60v except during Clear T when it rises to +li:;Ov. We ob-
serve that the voltage of the left grid of the 6j6 in the center is con-
strained by the 6AL5 bumper to lie between +75^ and +100v. Hence in all
cases the output voltage SO must rise to +120v during the Clear T (or
2 1
Clock) pulse, and at no other time can it exceed +100v. Now consider the
left 6j6. During a write cycle its left section is obviously held in a cut-
off condition, while its right grid is held at -20v from the beginning of TD
to the beginning of CI, when it rises to +10v, where it remains until the
beginning of the next TD pulse. Thus from the beginning of TD to that of CI,
the voltage of the left grid of the center is +100v, while the rest of the
time it is +75v. Thus SO is +120 during CI T at the end of which it falls
2
1.
to +75v where it remains until TD, when it rises to +100, falling again to
+75^ at tlie beginning of CI.
Comparison with the wavefcnns deduced as necessary for the operation
of the Discriminator (Fig. 2^) shows that the circuits we have been discuss-
ing should produce these subject to finite times of rise and fall of the
pulses. The actual waveforms obtained are shown in Fig. 25- The rise times
of the pulses are approximately .25 ^s in all cases; no serious distortion is
present, but a delay of approximately .O^^sec io introduced by the circuits
which is obviously too small to show in the drawings.
WILLIAMS TDBE DEFLECTION (ffiNERATCS^
We have seen that each storage tube holds an array of 12 x 32. bits of

<!-- p. 114 -->
lOi.
infonnaticn. The address of a bit consists of two numbers, each being one
of the integers 0, 1, ..., 31 (each, of course, expressed in binary notation)
which specify the horizontal and vertical coordinates of the bit.
An address is presented to the memory organ as the contents of a ten
stage binary register, the stages 2 2 ..., 2 specify the horizontal co-
, ,
ordinate, and 2^, ..., 2^ the vertical one. These binary nximbers must be
converted into the voltages needed to deflect the electron beam: this is
the function of the Deflection Generator, a schematic of which appears in
DWG. No. I28U and DWG No. I285. Before going on to a description of the
operation of this circuit, it should be mentioned that the twitch is treated
as an extra digit column in the horizontal coordinate: 2 is treated as the
highest order column, 2 the next and so on, with the twitch of order lower
than 2 .
The terminals at the bottom of DWG No. 1284 present to the deflection
genei*ator the twitch voltage (a pulse rising frc»n -20v to +10v in synchronism
with the rise of TD, and falling again in synchronism with the leading edge
of CI), and the digits of the address (+5v for a 0, -30v for a 1). The lat-
ter values are due to the fact that connections to the input terminals cone
from the address register by coaxial cable, which is driven by a cathode fol-
lower the input of which is taken from a toggle grid; cathode rise of 5' in
the cathode follower accounts for the values quoted here.
In order to minimize noise that may enter the deflection generator,
the full variation available at each Input terminal is not used, the diode
bumper, which is shown as the tube at the bottom of the left column in DWG
No. 1284 restricting the swing toCBefrom Ov to -lOv (these are, therefore,
the nominal values for and 1, and for twitch on and twitch off).

<!-- p. 115 -->
10.
TIow consider the 6j6 that appears Just abcve the input bumping diode.
As its left <5rid 1g held at -"pv, the left section will be non-ccnductinrt when
the right grid is raised to Ov, but conducting when the right grid is dropped
to -lOv. In the former case, the voltage at the right grid of the second 6j6
(fourth tube up) is bumped at +120v by the 6AL5- In the latter, it is bumped
at +100v (we note that the plate current of the left section of the first 6j6
must be somewhat greater than 95/13000 =7-3 ma, so that the plate voltage
will surely fall below +100v).
The second 6j6 in the column has, therefore, as input to its right grid
+120v for twitch on, +100v for twitch off. As its left grid is held fixed at
+110v, the left section will not conduct in the first case, but will in the
secoad, drawing a plate current of somewhat over ^.07 ma. As regards the
right section, the situation is reversed: in the first case a plate current
of somewhat over h.hk ma is drawn, in the second it is cut off.
Hence the voltages of the left and right plates of the 6j6 are, respec-
tively, for twitch on, kOOrt 382.7v; for twitch off, 38U.lv, UOOv.
,
In the first case the 12AX7 in the upper left-hand comer of the draw-
ing will have its left section on and its right section off; in the second
case the reverse will be true. Thus it will draw a current I = 100/R (where
E is the resistance in the cathode circuit) from summing bus A, and none from
B, while in the second these will be interchanged. In practice the variable
5C0K resistor is adjusted to maximize the amplitude cf the dash output of the
Willisuns Memory Output Amplifier, which depends upon the magnitude of the dia-
plac§ment between the A and B positions.
The operation of the other columns of tubes, which exactly duplicate
\the one we have discussed in detail, except for the tube type and the value of

<!-- p. 116 -->
103.
the cathode resistor of the top tube In the colximn, is, of course, identical
with that of the first column except as regards the current drawn from the
Slamming buses A and B. Thus in each case a input to the column results in
the drawing of approximately 100/R amperes from bus A and no current from B,
'while for a 1 input these will be interchanged. Taking account of cathode
rise in each of the tubes, the design values of the cathode resistors were
chosen so that the 2 stage would draw i = 6.98 ina; stage 2 , i = I/2 i ...;
k h
stage 2 , ih = 1//2 i^,. These currents are added in the summing buses, the
object being, of course, ultimately to cause them to flow through a resistor,
so that the voltage developed across this will be proportional to the binary
number used as input to the generator.
However, it is desired to make the currents developed available at a
higher voltage level (+1290v). This cannot be done merely by connecting
resistors in series with the summing buses directly to the +1290v voltage as
this would cause the tubes whose plates are connected to the buses to operate
with excessive plate voltage,"'so a rather simple scheme, consisting of four
triodes in series for each bus, was adopted. This is shown in DWG No. I285.
Here we have two columns of 5687's, giving, therefore, four columns of tri-
odes; the cathodes of the tubes of the row at the bottom of the drawing are
connected to the four summing buses A, B, C, D of DWG No. 1284. The grid
voltages are held at +4oov, +6lOv, +8lOv, and +1030v by means of the voltage
divider, consisting of a UOK, three 33K, a 27K, and a 33K resistor connected
between +1290v and ground. Condensers are placed in parallel with the re-
aiat-ors so that when the high voltage is turned on the grids will instanta-
neously assume their correct potentials. The parallel PC circuits between
the points feeding the grids and the heaters, hold the heaters at the d.c.

<!-- p. 117 -->
.
101+
level of the grids, so that the potential difference between each cathode and
its heater will be araall. The condensers guarantee that the heaters assume
the desired potentials instantaneously when the high voltage is turned on.
The top triode in each column is connected through a l^.yK resistor to
the +I29OV bus. Each summing bus current flows through one of these, and
hence there is developed across it a voltage proportional to this current.
The voltages at the lower end of these resistors are the deflection voltages:
thus A and B drive the horizontal deflection plates of the GET 's, and C and D
the vertical plates. Each deflection voltage is applied to all forty CET's
in i)arallel by means of a deflection bus. The two cathode followers in cas-
cade shown in the upper left-hand corner of DWG No. I285 provide the low im-
pedance source needed to drive the rather large capacity of this bus.
We observe that a in any digit position of the horizontal address
causes the drawing of current from the A bus, while a 1 causes it to be drawn
from the B bus. For the vertical deflection system, a corresponding remark
is true of C and D. Suppose the horizontal address is 00000. Then i(l + l/2
+ l/k + 1/8 + 1/16) = 13.52 ma is drawn from the A bus, and ma from the B
bus, and the deflection plate voltages are +1238.6v and 1290v, respectively:
These are, of course, reversed in the case of the address 11111; in both cases
the average value is +126U-.3v, or 25.7v below +1290. This condition holds for
all addresses, as the average of the two deflection voltages must always be
1/2 (1290 + 1290 - i(l + 1/2 + lA + 1/8 + 1/16) X 3-8), where i is in mil-
liamperes; the design criterion here was to hold the point half way between
the deflection plates constantly at the same potential as the second anode.
Clearly, it is necessary that we consider both the horizontal ajid the vertical
deflection plates: the potential of the point must be the same when referred

<!-- p. 118 -->
.
10?
WG
to either set of -^laton. The circuits ah^vn In No. 12SU^ labelled
"Average Deflection Plate Level AiijuGtment" rerr-.tt those potent^.ula ',o
be eoiiallr^ft'l• Moreover, the^e circuits guarantee that 8->rTie c irrent is
flowing in the busea A, B, C, D, at all times, bo that the tubes in the
vertical chain are never operated very close to cut-off.
WILLIAMS f-Er-OTT LOCAL COTTTEOL
A i^in^ie chnssic holds part of the Pulse Routine Generator, which
has already been nescribed, and the Williams Memory Local Control. It
also includes circuits, shown in DWG No. iUyo and C-l'+Y'*, for generating
-B, -TD, and the Strobe (which is an inverted and macnified version of
the Inspect pulse (I)). The Local Control echemattc is given in IWG No.
C-II+7H, to which reference ie made. A block dia.p-ara is f,iven in Figure 26.
Generally speaking, the Local Control receives from the Main Control
olgnala which signify whether or not the Memory is to be consulted in the
nert cycle, and whether information is to be Inserted in or ertracted from
it. It uses this information to cause the routine ,<^nerators to emit the
appropriate pulse trains, and to route back to the Main Control properly
timed pulses, originating In the Pulsera , which the Main Control can use
to clear RITI, open p^tes into RIII, and to gate address information out
of either part of the order counter or from R to the Villiams Tube deflec-
tion circuits as may be desire-'l. Local Control hIso returns to Mi^in Con-
trol signals pcknowlodging the request to use the Memory, and Blowing that
the rrocesn ordered has been completed. The Local Control serves tr co-
ordinate the (jenerrlly asynchronous operation of the rest of the computer
with tho carefully timed operr.tion of the Willinna Memory.

<!-- p. 119 -->
.
DC
The in^.jta tc t\v: Lcc.l Ccntrcl "one frcrn two oourca: th«^ Ki;ln
Ccntrcl end t.e ? ;"L3erj. Maj.n Cortrol Ei;.::ll°3 the? lt23/^'o ar/l Beif/ftrite
cJ.fTSP.ls, bfth rutiuts EJ3JLnJ.n;3 levels of -i'Ov and Ov. "Yes" signifies that
the Metncry is to t-.? consilt'^*? duririi,-, the next c/cle, vhicli ir, therefor'-,
called an "urtion" cycle ^ while "No" aignlflee that the Me'nory will not be
conaulted end thi:t a ref;ener3,tion cycle will, therefore, ensue. Ordinarily,
action and re»ienersticn cycles follow each other in sequence, the one excep-
tion being in the c^.oe cf that tj'pc of action cycle which ve shall cell a
"fetch" cycle, which occurs whenaver the second order in the word standing
In E l-ias been executed and it becor.ec necessary tc bring the next pair of
orders frc/ic tho ^'eraory tc E^. In thli; case it is pcrcittcd that a fetch
cycle be followed by a second action cycle. To assure that an acticn cycle
is to follo-i.- a regenerate cycle the Yes Gif^nel taust be received before the
TD pulse oi' the regenerate cycle, while the Read/Write information must be
received bc-rrrc the time of the B pulse. V/e shall eee that the Ycl'/Nc input
is always set to Kc by the Acknowledge Yes pulse emitted by the Local Control
ai the tir«o of this sario B pulce. If an action cycle is to follow a fetch,
it Is necessary thrst a Ygg si.^nal be received before the A rulse of the
fotch cycle.
The reiiaining inputs to the Local Control are received from the Pulsars,
or are built, up locPlly from then: thus TD^ , A. CI, CL-, . are used directly,
'1
while the other circuits shown in IWO No. C-IU7U invert B and TD to provide
inputs of -B and -TD.
The outputs of the Local Control are: A B ACl BCl A^, B ACL,
, , , , ,
BCL, "Finish", "Acknowled^ Yes", CIRIII," "Gate into Bill" to the Main Con-
trol, and a "Vrite/Read" signal to the Pulse Routine Generator (the first eight
of these are used to operate the Dispatch Counter in the Main Control)

<!-- p. 120 -->
107.
Circuitviae, the Local Control consists of three to^clec and a rather
complicated system of sates The oyeraticn of the circuit can beat be made
.
clear by reference to the logicel block diagram ^iven In Fi^. ^6. We use in
it the conventional recresentatioiis of the toggle as a box and of the gate as
a circle with two arrowhead inputs and one output. An Input to a gate from a
grid of a toggle signifies tliat the gate is enabled when the grid is high, but
disabled when the grid is low. In the actual circuit the arrangement is
slightly different, in order to take advantage of different gating arrangements
needed to give different voltage outputs, but once the logical structure is
understood, the schematic (DWG No.C-l'4^7'^) will be found readily comprehensible.
Note that the Action and Routine toggles differ slightly fron those used
throughout the machine in. that the crossover resistors are ench replaced by
two resistors in series, the output being taken from the point between them.
This results in an output of +10v from the conducting half of the toggle tube,
and of -20v from the non-conducting half.
Having disposed of these preliminary remarks, we now turn to an explana-
tion of the operation of the Local Control, basing our arguoent en Fig. 26.
Let us assume that the Synch, Action, and Routine toggles are all in
their states; I.e., the neon bulbs are not glowing.
Suppose that an action cycle is called for, signified by the Yes/No in-
put assiminp- its Yes level before the arrival of TD Then the gate into the
•
Synch toggle is enabled, and TD causes this toggle to assume its "on" state
(neon bulb glowing) This in turn enables the gate into the Action toggle,
.
which-is turned on by the A pulse. The grid of the right-hand section of the
Action toggle tube now is high (+10v} while that of the left-hand section is
low (-20v), and the gates connected to the right-hand grid are enabled, while

<!-- p. 121 -->

![Figure 26 — Williams Local Control Logical Block Diagram](images/fig_26.jpg)
*Figure 26 — Williams Local Control Logical Block Diagram*

<!-- p. 122 -->
:
109-
those connected oo t'.ie left-liand -rid arc disabled. Thuj the roliov^ing
sequence of events ensues
1) BCl io emitted, and the SjT.ch toci;le t'lmed off;
2) B. and Ackncwlcdje Ye^ are emitted, the latter returnin^:; the
Yes/Ko toggle in t^:e Main Control to the No conditicp.; furthernore, if Head-
ing is called for, B ic paiJoed on as CIRIII, end the Routine tosgle left in
the Read condition, vrLile if Writing is culled for, B fli-o the Routine tog-
gle to the Writ? condition:
3) ACl
A
is eniitted in synchronisa vith Ci,.',1, at the teglrjiint^ of the
next memory cycle;
h) A is emitted in SiTichrcnisni with TD of the next neraory cycle;
A
if Reading is cal].ed for, A nlso causes "3?'.te into RIII" to be emitted;
5) The Tes/Kc toggle l*.ving been set to He, the left gate iutc the
Action toggle is open, and the toggle is turned off by A, thus enabling the
whole set of gates in the left column;
6) The Finish signal is omitted;
7) BCL ia emitted;
8) B_ in et.rJtted, and the Routine toggle 3et tc the off (Read) condi-
tion if It is not already iv. that condition; thur the performance of an en-
sulnr; Regenerate cycle ia assured;
9) ACL is emitted in synchronism with CI— ;
10) A is exitte<3 in sjTichroniaci with TD.
Thus ve see that ordinarily a Regenerate cycle follows an Action cycle;
however, in the case of a fetch, the Yes/No toggle ic aet to Yes before A in
the fetch cycle, which prevents the turning off of the Action toggle, and thus
assures that the subsequent cycle will also be one of action. We note that in

<!-- p. 123 -->
110.
our sequence of evento, after 3) all the toggles have been set to their
off condition and will remain ao at least until after 10) , since if an
Action cycle is to be called for, the Synch toggle cannot be turned on
until TD
.
Complete diagrams are given in Figures 2? and 28 illustrating
the operations that have Just been described. Figure 27 shows the tL-ae
variation of the volta^ inputs and outputs for the following sequence
of cycles: Regenerate, Write, Regenerate, Read, Regenerate. Figure 28
does the same for the sequence: Regenerate, Fetch, Write, Regenerate.
Finally we observe that the transmission of information from the
Memory into Bill is directed specifically to R"^ (number or Work Order)
or R, (order or WO) by the WO sij^nal from the Main Control.

<!-- p. 124 -->

![Figure 27 — Williams Local Control Timing Chart #1](images/fig_27.jpg)
*Figure 27 — Williams Local Control Timing Chart #1*

Ill-
4.
c
p
C
U-
c
i
P
>
s
S!^

<!-- p. 125 -->

![Figure 28 — Williams Local Control Timing Chart #2](images/fig_28.jpg)
*Figure 28 — Williams Local Control Timing Chart #2*

112.
Mg^MMgmttf
—
J \ •
I \
I
!_
TT^
Attion J 1.
—
_-_^_. L -if. f-
'•:-i
—
Y.i y-T :i-T-nL.J-_l, i-r H-
,.!
AT
T-±zrd/z J:^
3-^
LT — n/: TT
A, u: •+— < I-
Lz:
V u
V3
±i:
"Tj-IL
V '
v:
J—
"LT nuz:! 4.
,i:.t
Urnittxrtt/a ! .. . 1
so,
6C,
SA,
f.„.A

<!-- p. 126 -->
iii.
VI. THE CONTROL
We have describe^i tiie Willlanifl Memory in eone detail, and have
shown how the Local Control regulates its operation subject to informa-
tion received from the Main Control. This inforioetlon must be of two
kinds. First, it is necessary to specify whether an Action or a Regen-
erate rycle is to be r»erfonned, and whether information is to be in-
s-i-rtod in or extracted from the Memory. Second, it is necessary to sup-
ply to the deflection circuits the address in the Memory of the bits of
inforraation which are to be written, read or re(generated.
Beaides supplyinjj orders and address infor.-nation to the Memory
Or»^n, the Main Control alao must regulate the actions of the Input-
Output Or.^an and of the Arith.'aetic Organ. Most of the equipment for
the latter function has been built and installed, and will be described
under the headings: "Oete-Clear Sequencing Chain" "Shift Counter",
,
and "Becognition Circuits".
THE SHIFT COUNTER
Two types of cointer are used in the present machine. These are
tne familiar "scaling" type, of which the Shift Counter is an example,
and the "adder" tyie , which operates as an Adder to which one input is
the last count and the othor is a 1 to the lowest order stage. The
Scaling type of counter has the advanta,^ that the more significant
stages can be comparatively slow, and that all the carries resulting
from one count need not be completei before the next count arrives at
the input, whereas in the Adder typo, all carries re8ultin-3 from one

<!-- p. 127 -->
113a.
count must be cora^^leted before the next count la added. On the other
hand, the Adder type offers the advantage of requiring fewer tubes.
Hence, thp character of the particiLar op.^llcation indicates the ap-
propriate type of counter. In the Di?a;iatch Coariter the complete now
address muat lie obtainnd before the counter is step;)ed aijain, so that
the Adder ty"_je Is obviously aprropri-ite, while in the 3hlft Counter
this is not trie, so that the Sculins type is used.
The Shift Counter is ;)art of the aquipnent used to control the
carrying oit of the arithmetical processes. Thus nultiplication la per-
formed bj' the s.icce3sive additions and shifts. Once the process is
initiated, the Shift Counter counts the 9uc::es3ivo shifts. The number
of these which mujt be Tierformed is inserted in the Recognition circuit,
where it is continuously compared with the contents of the Shift Counter;
when coincidence is indicated.

<!-- p. 128 -->
IIU.
a signal is emitted which terminates the process A similar situation oc-
.
curs in the carrying out of division.
Physically the Shift Counter consists of two rows of toggles with
gates permitting information to be transferred up and down vertically and
up diagonally. One row of toggles holds the actual count, the other does
not; these are referred to as the True and False rows, and the numbers they
hold as the True and False counts, respectively. It will appear that the
False count does not proceed monotonically. There are six stages in the
counter, those for 2 2 1 ..., 2^"i. Since the counter must only count to
, ,
forty (the number of additions inthe multiplication process) the 'P stage
can be rather simpler in structure than the lower order stages; it is feas-
ible to have but a single toggle in this sixth stage.
Before examining the schematic of the counter, let us consider the
block diagram of a single stage, given in Fig. 29(a). This represents any
of the stages 2 to 2 . It has already been remarked that the sixth {'P)
stage is of simpler structure; it will be considered later. Here input E '
n
enables gates from the True to the False toggle, which are so arranged that
the enabling of the gates causes F to assume the same condition as T. On
the other hand, input E " enables gates leading from F to T in such a way
that the enabling of the gates causes T to assume the condition opposite to
that of F. At the input to the 2 stage, the levels for E ' are Ov to dis-
o
able, -20v to enable, while those for E " are +60v to disable, +110v to en-
able; in the following stages the levels of E ' become Ov and -35^, and those
of E " remain substantially unchanged. We will have more to say on this sub-
n
ject when we discuss the circuitry.
The input to the lowest order (2 ) stage of the counter consists of

<!-- p. 129 -->

![Figure 29 — Deflection generator stage circuit and input waveform](images/fig_29.jpg)
*Figure 29 — Deflection generator stage circuit and input waveform*

i-l?"
a
ci
^
/>;
-^ ^
^n
-^ ^ "U)
f>7 ^ -^^,
\
cu\ /_cj
-"VvV Vav-
7;; -^
L
^/T
r^;
—
-20 ---- ' - ' - - -
+110
£-'' f«o
^
Infur TO Z" 3TACre.
M
W/cuR-E 2*7

<!-- p. 130 -->
U6.
the pair of pulses shown in Fig. 29(b) for each item to be counted. The
number held by the counter is presented to the recognition circuit, which
is physically located on the same chassis, as a set of six voltages, one
for each stage of the counter, the presence of a being signified by Ov,
that of a one by -^v.
Bach stage of the counter, therefore, has two inputs and three out-
puts; on Fig. 29(a) the inputs are designated E n ' and E n ", the outputs E n,
E' n+l- , E" n+i. Of these E n signifies to the recognition circuit the contents
of the stage, while E' , B" are inputs to the next stage. In the ac-
tual circuit, DWG So. I289, let us lab#l the tubes TIJ, where i signifies
the row and J the column in the array. The first five columns and the
lower three tiibes of the sixth form the actual counter. The upper four
tubes in the sixth column are clear drivers used to clear the two rows of
toggles. Consider the first column. T is the F toggle of the block dla-
grsun, T is the up gate, T, the down gate, T the gate driver, while the
21 Ivl 31
lower three tubes, T T^ T are the T toggle, which is actually what
51, 61, 71
we have before termed a Supertoggle. It is used in this instance because
of the speed with which it can be caused to switch from one state to the
other.
The counter is prepared for operation by clearing all the T toggles
to and the F toggles to 01111 (2 holding a 0, the others I's). Consider
the first column. The first pulse of the input pair clearly does nothing,
for in this case both T and F already hold O's. On the other hand, the
down gates transmit a 1 to T if F holds a 0. Hence after the reception of
the pair of pulses T holds a 1.
Now let us consider the influence of the n-th column of the coxinter

<!-- p. 131 -->
.
117.
upon the (n+l)-th. According to the block diagram of one stage, the gating
voltages (1) aind (2) to the next stage are the left grid and right plate
voltages of the T toggle tube. Hence vhile this toggle holds a 0, (1) and
(k) are both at their high level with the result that in the next colvunn
the up gates are disabled and the down gates enabled. On the other hand,
when T holds a 1, the gating voltages are both held at their lower values,
with the result that the up and down gates of the next stage are, respectively,
enabled and disabled.
aloraOlfF
Thus if T n holds a 0, T n+l must hold n+,i-,. holds a or a 1,
while if Tj^ holds a 1, the contents of F ^^ must coincide with that of T ,
These facts mean that whenever T holds a its next change of condition to 1
n
cannot change T n+1,, but does cause F n+1, to agree with T n+l, while whenever
T holds a 1, its next change of condition to cannot affect Fn+]^> t)ut must
cause a change of condition in T n+1. Thus two successive changes of condition
in T_ " cause a single change of condition in T n+1, so that the perfonnance of
the circuit as a binary counter of the scaling type is guaranteed.
We will now consider the actual circuits involved, and in particular
will show how the simplified sixth stage of the counter works, and how its
simplified form restricts the number of items that can be counted without
impairing the usefulness of the counter in its particular application.
The toggles of the False rank and that in the sixth stage of the True
rank are of the type encountered throughout the computer, while the first
five toggles of the true rank are the so-called Supertoggles. The gating
arrangement from T to F is quite straightforward; we describe it for the
first column, the remarks obviously also applying to all others but the sixth.
Each gate consists of one section of T and the left section of T . From

<!-- p. 132 -->
113.
the way in which the grids of the toggle tube T^, ore returned to -'iOOv, it
is readily seen tliat when the voltage of a grid of the toggle tube Is Ov,
that of the corresponding grid of the gate tube T is approximately -lOv,
while when the toggle grid voltage is -UOv, that of the gate grid is approxi-
mately -li.8v. Hence, if the grid of the left section of T is held at Ov, it
31
is clear that the cathode of T is held so far above that of either grid
21
that conduction is impossible, while if the grid voltage of the left section
of T is dropped to either -20v or -40v, that section of T^, will conduct,
31 ' 21 '
the grid voltage of which is Ov, while the other section will remain cut off.
Now consider the "down" gates, each composed of the right section of
T and one section of T. . The grid voltages of T. ^ are either Ov or -UOv,
while its cathode is returned to ground, and both plates are connected to the
right cathode of T through 5.6K resistors. While the voltage of the ri^t
grid of T is held at 60v, that of the plate of the conducting half of T,
is substantially below 60v (apart from cathode rise in T^.)
.
The plates of
T are connected to the left grid of T^, and the right grid of T the
51 71,
1*1
other grids of these tubes being connected to the plates of the Supertoggle
tube, T^ o , l. Hence, while the gating voltage E o " is held at 60v, neither plate
of T. . is effective in determining the cathode voltage of T or T_,, and
the Supertoggle can remain in either condition.
Now suppose the voltage (2) to be raised to +110v, bringing with it
the voltage of the plate of the cut-off section of T, . Let us assume that
F holds a 0, so that this is the rig^t section of Tj^^: the plate voltage
of the left section also rises to about 60v. Suppose now that T holds a 1,
so that the grid voltage of the right section of T , is about 460v, and that
of the left section of T is +110v. The grid voltages of the left section
71

<!-- p. 133 -->
U9.
of T , is about +60v, and that of the left section of T™, is +110v. The grid
voltages of the left section of T^
5
,
1
and the rig°^ht section of T,
7
,
1
are aloe +60v
and +110V, respectively, so clearly nothing happens. On the other hand, if T
holds a 0, the grid voltages of the right section of T^, and the left section
of Ty^ eire +110v and +60v, respectively, and, therefore, the cathode voltage of
T_^ is raised to +110v, the voltage of the right grid. Clearly this flips the
supertoggle to the 1 position. Similarly, if F holds 1 and T 0, the raising of
the gating voltage E" from +60v to +110v does not affect T., but if T holds 1,
it causes it to flip to 0.
The discussion just given applies to the columns 2^, ..., 2^. The 2^ col-
umn is simpler in structure, consisting of three 2C51 tubes: T^, T/-^, T„/-, of
which Tgg is the toggle tube, the other two performing gating functions. Inputs
are: from the left grid of T^^ to the left grid of T^, and from the ri^t grid
of Tg^ to the left grid of T_g.
Suppose O's exist in the 2 emd 2^ stages. Then the left section of T^^
55
is cut off, and the right conducting, the cathode voltage being -UOv. The left
section of T„g is conducting, the cathode being Ov. Nov consider the right sec-
tion of T-g, which is connected as a diode. The plate is connected through a
U.7K resistor to the cathode of the left section,.and the cathode is connected
directly to the cathode of the right section of T^. Hence, the ri^t section
of T„>- conducts, and its plate voltage, which is the output from this stage to
the recognition circuit, is not much above -kOv.
How let the 2 stage toggle flip to 1. The cathode of the left section
of T-y- now falls to -UOv, eind as the cathode of the ri^t section cannot fall
below this voltage, the output remains at -ko^. The left section of T^g conducts,
and the usual gating action takes place, the toggle being flipped to the 1

<!-- p. 134 -->
lA).
condition. Thus flipping the toggle in the 2 stage to 1 automatically flips
the toggle in the 2^ stage, but does not effect the output voltage, irtiich re-
mains -^v, signifying a 1.
This condition persists as long as the 2^ stage holds a 1, hence, up to
and including the count of 31- On the count of 32, stages 2 , ..., 2 must all
return to 0. The left section of T^ is now cut off leaving the toggle in the
1 condition, and the cathode of the right section, and hence the cathode of the
rig^t section of T„g, rises to Ov. At the seune time the cathode of the left
section of T^g rises to Ov, and we are assured that the ri^t section of T™g
will not conduct, and its plate voltage, therefore, becomss Ov, signifying a
1 to the recognition circuit.
The lower order stages now proceed with the count, the 2^ stage remain-
ing in the condition until the count of k8, ^rtien it flips to 1. We have
already seen, however, that if both the 2^ and 2^ stage toggles are in the 1
condition, the 2^ stage output voltage drops to -^v, signifying a to the
recognition circuit. The shift counter cem only count to ^7* returning to 32
on the count of k&. However, since the Shift Counter is only required to count
to ^K), this is no limitation on its usefulness. The recognition of this fact
permits the simplification of the 2'^ column, with attendant saving in tubes.
The space thus saved is occupied by the two clear drivers T^g, T^g, and the
cathode followers Tp^, Tj^: Tp^ permits all the plate current for the F tog-
gles to be drawn from the -«-2^v bus, thus holding this current constant and
preventing any fluctuation of plate voltage due to current fluctuation in the
power supply and bus impedance, while Tj^ accomplishes the same for the T tog-
gles and the +220v bus.
Fig. 30 shows the contents of the F and T toggles as the counter pro-
ceeds from its quiescent condition to the co\int of forty. In the T column

<!-- p. 135 -->

![Figure 30 — Shift-counter / recognition-circuit truth table](images/fig_30.jpg)
*Figure 30 — Shift-counter / recognition-circuit truth table*

<!-- p. 136 -->
122.
the symbol [ij ia used to Indicate that, though the toggle is In the 1 condi-
tion, the output is so arranged as to present a to the recognition circuit.
RECOONITION CIECUIT
The function of the Recognition Circuit is to compare the number in
the True rank of toggles in the Shift Counter with some predetermined number,
to determine when the two coincide, and at that instant to emit a signal which
can be used to terminate the process the number of steps in which is being
counted.
Since the "number to be recognized"and the number in the counter are
both six place binary numbers, there are twelve inputs to the Becognltlon
Circuit. Six of these are the output leads from the True rank of Counter
toggles, and six come ultimately from the read-out gates of B . There is a
3
single output, the signal emitted when the number in the counter has increased
until it coincides with the "number to be recognized."
The Shift Counter chassis contains the Recognition Circuit, and also
the Address Dispatch Gates,which will be described later on. We refer to
DWG No. 1289 for the schematic.
The Recognition Circuit itself consists of the the last six tubes in
each of the two lowest rows in the drawing * : T- 6 - 7 ^, . . . , T, 6,12, and T 77 , ....
T . The inputs labelled (A) are clearly from the Shift Counter, while
the voltages representing the "humber to be recognized" are brought down on
the leads labelled (B), these voltages being developed in the cathode cir-
cuits of the input cathode followers T^ 2,8 o ' , . . • , T 2,12
Each of the tubes T „,•••, T is a 2051, the two sections func-
2,8' 2,12
tionlng Independently as cathode followers. We observe thAt each grid is

<!-- p. 137 -->
123.
t connected to the +110v bus through a 7'5K resistor and to the input lead from
E . The llOv bus la the plate supply of the Bill Green gates. Since all ten
cathode follower circuits are identical, let us consider one in detail.
Suppose, for example, that the 2 toggle in B contains a 0. Then
the opening of the Bill read out (Green) gate has no effect on T since
2,8-,,
no current is drawn from the +110v bus. The voltage of the left cathode Is
+110V, and, if the grid of the left section of T were not connected to the
point between the I5K and the two 22K resistors in the cathode circuit, the
voltage of this point would be approximately +6v. With the grid connected
as shown, a alight grid current is drawn, and the voltage of the point is
reduced nearly to Ov; we consider it to be Ov as this is sufficiently ac-
curate for our purpose.
If we consider the effect of a 5^ tolerance in the values of the I5K
and the two 22K resistors, it turns out that without the grid connected, the
voltage at this point, assvunlng that the cathode of T „ ±b +110v, can be as
2,0
low as -2v and as high as +13v. Hence with the grid connected, no grid cur-
rent is drawn in the first extreme case, while in the second, about twice
the nominal value is drawn. Thus one would expect considerable variation
in plate voltage from tube to tube for a input: measured values nin from
9v up to Ikv with the average of 12.8v. This variability, however, is of
no consequence: we will see in our discussion of the Address Dispatch Gates
that the plate ,voltage under discussion must only fall below about 20v for
satisfactory operation.
On the other hand. If the 2 stage of B contains a 1, the opening of
the Bill read out (Green) gate causes a current of 5 "»•• to be drawn from the
+110V bus, which reduces the voltage of the left grid of T g to +72.5v- The

<!-- p. 138 -->
ISk.
voltage of the left grid of T accordingly falls to a nominal value of -22v,
outtlng off the left section of the tube. The actual value is, of course, dif-
ferent from the nominal one for two reiasons: cathode rise in T and permitted
2,8 *^
tolerances in the I5K and the two 22K resistors. Measured values range from
-17.5v to -20.3v at the ten grids of T .,...,? Actually even -I7.5V
3,0
3,12.
is about twice the value needed, as we shall see.
We have seen, therefore, that if a is held in the 2 position of B-^,
the nominal voltage on the corresponding lead (B) is Ov, while if a 1 is held
there, the nominal voltage becomes -22v.
Let us now turn our attention to the Recognition Circuit proper. We
suppose some "number to be recognized" has been chosen, the voltages represent-
ing its digits (Ov for 0, -22v for 1) being applied as inputs to the gfrids of
^
the ri^t-hand sections of T^ „,..., T These Inputs are established
7,7' 7,12.
vith the counter in the quiescent state, all outputs (A) representing O's.
We assume that the "n\amber to be recognized" is not 0. Therefore, at least
one input (B) is -22v, and thi» voltage is assumed by at least one of the
cathodes of tubes T_ _,•••, T hence, at least one section of the 6AL5's
7*7 7,12;
T , T , T is in a conducting state, with plate voltage slightly above
6,8 6,10 6,12
-22v, and either the right section of the 2C51, T^ or one section of the
,
6j6, T^ is cut off, with plate voltage, therefore, at +110v. From the
6,11,
tube characteristics it can be seen that for both types used here, with
grounded cathodes, lOK plate load resistors, and +110v plate supply voltages,
cut off occurs when the grid is dropped slightly below -kv. Thus the -22v
available is more than ample, and even -lOv would provide an adequate margin
of safety. Therefore, either the left section of T^ is conducting with
cathode voltage at +110v or one section of T, is conducting with cathode
6,9

<!-- p. 139 -->
185.
voltage at +110v; in either case the voltage of the point labelled "Out" in
the drawing must be +10v.
Let the coimting process now begin. At the count of 1 the cathode of
T must follov the left grid to Ov. If the "number to bo recognized" is
10000, then all the remaining cathode voltages are already Ov, and with the
cathode of T also assuming this value, none of the diodes conduct, all
their plate voltages assuming the value Ov. Then the right half of T, and
both sections of T/- ^- conduct, their plate voltages falling to about +60v
in all cases, vhich causes the voltage "out" to fall to -27v«
How consider an arbitrary "number to be recognized". Prom the previ-
ous paragraph it is clear that when the number in the counter reaches agree-
ment with it, the voltage "out" assumes the value -27v. We must still show
that the "out" voltage cannot drop to -27v until agreement is reached.
Consider two binary numbers n > m; if they ar« not of the same number
of digits, we fill in the missing higher order columns of m with O's -- this
is exactly what occurs in the case under discussion. First we compare the
highest order column: n certainly contains a 1 whAe m may contain a 1 or
a 0. If m contains a 1 there, we examine the column of next lower order.
Here either both numbers have a 1 or both have a 0, or if there is disagree-
ment, n must have a 1 and m a -- the contrary case is impossible, for then
we have m > n. Hence, as we move from the highest order columns on down, the
first disagreement we meet must always be between a 1 in the larger number
and a in the smaller. In columns of lower order than that in which the
first disagreement is found, obviously anything can happen.
Physically the last paragraph means that as long as the "nunber to be
recognized" exceeds the number in the True rank of the counter, at least one

<!-- p. 140 -->
126.
of the tubes T 1)1, ..., T 7>1^ will have its left grid held at -UOv and
its right grid at -22v, thus assuring a voltage of +10v at "out".
If the counter were permitted to count beyond the "number to be
recognized" the voltage "out" could assume either the -2Tv or the +10v
level in different cases, resulting in complete ambiguity. However,
there ia obviously no trouble here, as there is no point in continuing
the count beyond the number to be recognized which will not exceed forty,
and the "out" voltage is available to terminate the process, the number
of steps in which is being counted, as soon as agreement ia reached.
THE ADDRESS DISPATCH QATBS
^^
These are the tubes T^ 3, ..., Tj^ j^ and T^^g, ..., T^ -j^ 1-n
No. 1289. It has been shown in the discussion of the Becognltlon Circuit
that, for example, if 2° in R^ is 0, the left grid of T^^q assumes a value
between +9v and +lW, while if 2° in R^ is 1, this must become +110v. The
rl^t-hand grid of T^ g is driven by the left cathode of the 2C51 cathode
follower Ti^ 7* to the grida of which ia applied a voltage of +110v, which
ia caused to drop to +15v when it is desired to enable the gatea. Thus
a ia signified to tfe Dispatch Counter by +15v, and a 1 by +110v.
THE GATE-CLEAR SEQUENCING CHAIN
We have seen that the Adder and Digit Resolver form the sum of the
contents of R^ (or the complenant of this number) and R^^ and transmit this
sum by way of a set of g^tea (the Green gates of RI) to R^ As the Green
ffites transmit O's, it is necessary first to clear R^ to I's before opening
the gites, so that it is essential that these clear and gate operations

<!-- p. 141 -->
127-
should proceed in the proper time sequence.
The contents of B can now be transferred to H^ We recall that
.
the "shift do'-ra" operations shift the contents of B either one place to
the left or one to the ri(^t. In each case B, must be prepared to receive
the information treuismitted by B by the appropriate clearing operation.
Thus, for the left shift we tleeo- B^ to I's and "shift down left" O's
(Oreen clear and Bed g^te) , while for the right shift we clear B^ to O's
and "shift down right" I's.
The performauice of multiplication and division are facilitated by
the stiTict'ore of the registers. In multiplication the nultiplioand is
placed in B and the multiplier in B , B, being cleared to 0. Then if
^
the lowest order digit in B (i.e., the contents of 2' ) is 1, we add
the multiplicand to the contents of B^, shift this sum one place to the
ri^t, and put it back into B, . We then shift the multiplier one place
to the right and repeat the process if the new lowest order digit is a 1,
while if it is 0, we merely shift the contents of B, one place to the
,
right and do the same with that of B we are then ready for another step.
:
Similarly division la performed by a sequence of subtractions
and shifts.
Each of these recording and shifting operations requires the follow-
ing sequence: clear, gate, clear, gate: we refer to such a sequence as a
"cycle" of the Arithmetic Unit, and to a single sequence of cleajr and gate
as a half cycle. For convenience we record the possible operations:
Eecord (Accept): Bed Clear, Green Gate
Shift up (Beject) BlAck Clear, Yellow Gate
:
Shift down left: Green Clear, Bed Gate

<!-- p. 142 -->
128.
Shift dovn right: Yellow Clear, Black Gate
Obviously the first half cycle is either a "Record" or a "Shift Up", while
the second is either "Shift Down Left" or "Shift Down Eight".
The proper sequencing of these cle«a"ing and gating operations is the
function of the "Gate-Clear Sequencing Control", of which a schematic appears
in DWO No. 1287. We note that it consists of five main chassis, labelled
"CT Bot.", "CG Bet.", etc. For simplicity we nuniber these 1 to 5. Any tube
will be referred to as T. . where i signifies the number of the chassis, and
the number attached to that tube in the schematic. There is also a small
J
chassis "CX" containing two dual triodes and a dual diode. Normally the
switch in the lead to cathode (1) of T is set in the position which con-
nects this cathode to cathode (7) of Tpc- The single pole single throw
switches in the leads to cathode (^T) ofi*Tj^^ ^^^ ^o cathode (5) of the diode
on chassis "CX" are normally closed.
Inputs to the Sequencing Control eire the gate and clear voltages from
BI and the Counter Stop voltage, which is that labelled "Out" on the schematic
(DWG No. 1289) of the Shift Counter and Becognition Circuit. This voltage has
two levels: it remains at +10v until the counter contents agree with the
"number to be recognized", at which time it falls to -27v. Outputs are the
four voltages shown to the cathodes of the clear selector tubes and the four
voltages to the gate driver-drivers in BI and RII.
'Thu^, lt'«appears that the circuit generates signals which initiate gat-
ing and clearing operations, the results of which are fed back to it. One
will expect, therefore, that an action once initiated will be self-perpetu-
ating, and this is indeed the case. The Counter Stop signal serves to initi-
ate and to tenninate the process, eis will be shown.

<!-- p. 143 -->
,
129-
We first describe in detail the quleacent state of the circuit.
Suppose that the gate and clear inputs are all at their upper levels, that
the toggles in chassis 1 and ^ have been set in the 1 position (neon lamp
glowing) and that the Counter Stop voltage is at its lower level of about
,
-2Tv; which guarantees that grid (6) of T. is held far below cut-off and
consequently that the voltage of plate (1) is high (+110v).
Since the toggle in chassis 1 is in its 1 condition, the voltage of
grid (5) of T,K is approximately Ov, so that the voltage of plate (2) is
Bli^tly less than 50v, while grid (6) is far below cut-off, and hence the
voltage of plate (1) is +110v. The plates of T . are connected to the grids
of T,^, both sections of which are connected as cathode followers. From the
16
cathode circuit of the left section, outputs are taken to the grid of the
left section of 1-,=^ and to the grid of the left section of T^; similar
connections are made from the cathode circuit of the right section to the
grid of the right section of T and that of the left section of T^. The
voltage divider network from which these outputs axe taken are so designed
that when the cathode voltage assumes its hij^ value (approximately +110v)
a slight grid current is drawn by T and the grid is held approximately
at Ov, and consequently the voltage at the other end of the IK resistor
becomes approximately 7v. On the other hand, when tlie cathode assumes its
low level of voltage, the corresponding section of the T,g is cut off, the
grid voltage becoming approximately -3^'^> while that at the other end of the
IK resistor becomes -29v. Now consider the effect on T . Its grid volt-
ages are either -35v or Ov; hence, with a 5.6K plate resistor, the plate
voltages are either +110v or approximately +60v. The circuit in chassis 5
is exactly the seuae and so needs no further discussion.

<!-- p. 144 -->
. .
IJD,
The outputs of the supertoggle consisting of T. ^ and the tube moxmted
in the chassis "CX" are very simple: from the cathode (2) of the left sec-
tion of the latter to the grid (6) of T^l and grid (5) of T , and from the
cathode (8) of the right section to grid (6) of T 36 ^ and grid (5) of T 35 .
These cathodes can assume two levels: when the toggle holds a 1 the voltage
of cathode (2) is approximately 46OV and that of cathode (8) is +110v. We
assume that the Counter Stop voltage is at its lower level of about -27v,
which guarantees that the left half of the Supertoggle tube T. , is cut off.
We shall see presently that the other section is also held off under these
circumstances
We can now summarize the approximate voltages presented to the re-
mainder of the circuit by the tubes in chassis 1 and 5 *nd the supertoggle:
^26 grid (3):-29v grid (7):-29v cathode (2) :-29v cathode (8) :-2
grid (3):+7v grid (7):+7v cathode (2):+7v cathode (8):+7
grid (5):+110v grid (6):-f60v cathode (7) : +110v
33
grid (5):+60v grid (6):+110v cathode (7):+110v
^35 grid (5):(see below) grid (6):+110v cathode (7) :+110v
grid (5):+110v grid (6):(see below) cathode (7):+110v
^36
These tubes are all cathode followers; in T_ 2 ^ 6 and T^i,J/^- the Bectiona
are independent, but in each of the rest the cathode is common to both sections
so that the cathode voltage is in each case equal to that of the higher grid.
The voltage dividers in the cathode circuits of T , ..., T are so designed
33 36
that the output is +8v when one of the grids is high (+110v) and -l8v when
both grids are low (60v)
We now list the grid voltages of the tubes driven by the cttthode fol-
lowers listed above:

<!-- p. 145 -->
| | grid (5) | grid (6) | cathode (7) |
|---|---|---|---|
| T22 | +8v | +8v | +8v |
| T23 | -29v | +8v | +8v |
| T24 | -29v | +8v | +8v |
| II  T25 | -29v | -29v | -29v |
| T42 | +8v | +8v | +8v |
| T43 | +8v | +7v | +8v |
| T44 | +8v | +7v | +8v |
| T45 | +7v | +7v | +7v |

We also observe that the left section (cathode (1) and plate (7)) of the
diode T21 is in a conducting state. This holds the grid (5) of T41 below
cutoff, so that grid (6) of T36 and grid (5) of T35 are both held at +110v.

The output voltages are now easily obtained:

| | | | |
|---|---|---|---|
| To R1 Clear Selector | +8v | Red Gate | +8v |
| To R1 Clear Selector | +8v | Black Gate | +8v |
| To R2 Clear Selector | +8v | Green Gate | +8v |
| To R2 Clear Selector | +8v | Yellow Gate | +8v |

We recall that a positive input to the gate driver drivers disables the
gates, while a sufficiently negative one enables them. The disabling volt-
age of +8v becomes more positive after cathode rises in the cathode followers
which serve as gate drivers and gate driver drivers; in practice, the volt-
ages of the -300v, +110v, and +220v buses were all dropped five percent,
and the voltage dividers in the cathode circuits of the last four tubes in chassis
3 were then padded until the actual gating voltage was observed to be +10v.

Furthermore, we recall that the clear selector tubes are 6J6's whose
grid voltages are the grid voltages of the appropriate toggle, and are thus

<!-- p. 146 -->
132.
either Ov or -kOv , while the cathode of the tube is directly connected to
the Clear Selector output of the Sequencing Chain. With this cathode held
at +8v, obviously both sections of the Clear Selector tube are cut off, and
the clear bus voltage is held at +I5OV, while when the cathode is dropped
midway between Ov and -Uov, the section whose grid is at Ov conducts, while
the other remains cut off.
Hence,Ihe condition of the Sequencing Chain described above is a stable
one: no clears or gates eire generated and hence none are fed back to change
the condition of the Sequencing Chain circuitry.
Now let the Counter Stop voltage be raised from -27v to +10v. This
permit* grid (6) of T, to rise in voltage to Ov, beyond which it cannot go
(more than a few tenths of a volt) because of the grid current that starts
to flow. Thus, the supertoggle is put in the 1 condition and the voltage
of cathode (2) of the supertoggle cathode follower falls to +60v, which
brings the voltages of grid (6) of T and grid (5) of T^_ both down to 460v.
34 33
Referring to table I it is clear that this action causes the cathode voltages of
these two tubes also to fall to +60v, and hence grids (5) of T]^„ and Tj^, grid
(6) of T , and grid (5) of T all fall from +8v to -l8v. Reference to table
II now shows that the cathode voltage of T falls to -l8v, but those of Tj^^^
and Tj. are both cau^t at +7v by the other grids of those tubes. Thus the
net effect so far of the rise in the Counter Stop voltage is to cause the R
and r2 Clear Selector voltages to fall to -l8v: we need only concern our-
selves with the clearing of R^, as it is this voltage which is fed back to
the Sequencing Control.
Thus we have:

<!-- p. 147 -->
.
133
^26 grid (3) :-29v grid (7):-29v cathode (2):-29v cathode (8):-29v
r grid (3):+7v grid (7):+7v cathode (2):+7v cathode (8) :+7v
r grid (5) :+6ov grid (6) :+60v cathode (7):+60v
33
grid (5):+60v grid (6):460v cathode (7) :-f60v
grid (5):+110v grid (6):+110v cathode (7) :+110v
^36 grid (5):+110v grid (6) :+110v cathode (7):+llOv
whence
grid (5):+8v grid (6 :+8v cathode (7):+8v
22
"23 grid (5):-29v grid (6 :+8v cathode (7)f+8v
^21. grid (5):-29v grid (6 :-*-8v cathode (7) :+87
^25 grid (5):-29v grid (6 :-29v cathode (7):-29v
II
^2 grid (5):-l8v grid (6 :-l8v cathode (7):-l8v
^.3 grid (5):-l8v grid (6 :+7v cathode (7):+7v
grid (5):-l8v grid (6 :+7v cathode (7):+7v
%
grid (5):+7v grid (6 :+7v cathode (7) :+7v
and the outputs become:
To B Clear Selector -l8v Red Qate-
To R Clear Selector +8v Black Gate +8v
III'
2
To R Clear Selector -l8v Green Gate +7v
To Rg Clear Selector +8v Yellow Gate +7v
Whether the Red Clear (R^ to 1) or the Black Clear (R^ to 0) takes
place now depends upon whether 2~-^% holds a 1 or a 0, but obviously one of
t these must occur. Suppose, for example, that the Black Clear occurs, the
voltage of the Black Clear bus falling from +I5OV to +50v. Evidently this

<!-- p. 148 -->
13^.
also clears the toggle In Chassis 1 to 0, and we must trace the consequences
of this event. It is easiest to show these by another series of tables:
grid (3):+7v grid (7):-29v cathode (2):+7v cathode (8):-29v
26
grid (3):+7v grid (7):-29v cathode (2) :+7v cathode (8):-29v
1^
grid (5) :+60v grid (6) :4^0v cathode (7):460v
grid (5):+110v grid (6):+110v cathode (7):+110v
^3^
^35 grid (5) :+110v grid (6):+110v cathode (7) :+110v
^36 grid (5) :460v grid (6):+110v cathode (7){+110v
These cheuiges in turn influence the tubes in chassis 2 and k as follows;
grid (5) :+8v grid (6):+8v cathode (7):+av
22
grid (5):+7v grid (6):4av cathode (7):46v
^23
grid (5):-29v grid {6):+dv cathode (7):^8v
grid (5):+7v grid (6):-29v cathode (7):+7v
"25
II"
grid (5):+8v grid (6):-l8v cathode (7):+av
k2
grid (5):-l8v grid (6):-29v. cathode (7)i-l8v
\3
"1^ grid (5):+8v grid (6) :+7v cathode (7):4ay
grid (5):+7v grid (6):-29v cathode (7):+7v
Thus we have:
To E Clear Selector: +8v Bed Gate: +8v
To B Clear Selector: +8v Black Gate: +6v
III"
To B 2 Clear Selector: +av Green Gate: +5v
To E Clear Selector: +8v Yellow Gate: -iBv
2
Thus the Black Clear is terminated and the Yellow Gate enabled. Lags through
the circuits cause an interval of 1-5 usee to elaspse between the initiation
and termination of the Black Clear.

<!-- p. 149 -->
135.
The Yellow Gate which is now enabled is fed back to the Sequence
Control: the voltage of grid (6) of T drops to about -20v and enables
the other section to draw plate current: thie is, of course, the standard
gating procedure for reading into a toggle, and the toggle in chaaais (5)
is caused,to flip to its state. It is now neceasary to trace the conae-
qxiences of this, which we do again by listing the voltages throu^out the
circuit.
grid (3):+7v grid (7):+7v cathode (2) :+7v cathode (8) :+7y
26
grid (3):-29v grid (7):-29v cathode (2):-29v cathode (8):-29v
P grid (5):+60v grid (6):+llOv cathode (7):+110v
33
T 31* grid (5):+110v grid (6):+60v cathode (7) : +110v
grid (5):+110v grid (6):460v cathode (7):+110v
^35
•36
grid (5)i-»60v grid (6):+110v cathode (7):+H0v
Thus the voltages in chassis 2 and k are:
22
grid (5):+8v grid (6):+8v cathode (7):+8v
grid (5):+7v grid (6):+8v cathode (7):+8v
23
grid (5):+7v grid (6):+8v cathode (7) :+8v
^25 grid (5):+7v grid (6) :+7v cathode (7) :+7v
grid (5):+8v grid {6):-¥dv cathode (7) :+ev
U2
grid (5) :+8v grid (6):-29v cathode (7) :+5v
r grid (5) i+Qv grid (6):-29v cathode (7) :+8v
kk
grid (5):-29v grid (6):-29v cathode (7) :-29v
And so we have
To E Clear Selector: +8v Bed Gate: +8v
III'
To B Clear Selector: +6v Black Gate: +6v

<!-- p. 150 -->
136.
To B Clear Selector: 46v Oreen Gate:
Ill"
To B Clear Selector: +8v Yellow Gate:
2
eo that the Tellow Oate has been disabled. Again, due to delays In the cir-
cuitry, the disabling of the Yellov gate occurs about I.5 iisec. after its
enabling. Another effect is that since the cathode voltage of T. falls to
-29v* conduction takes place in the left section of the CX diode and in the
right*section of diode T , which causes the grid (6) of supertoggle tube
T, to fall below cut off. As cathode (1) of T is held at +7v, there is
.41 21
nothing to prevent the flipping of the supertoggle wfcich acconilngly assumes
its condition. This in turn raises the voltages of grid (6) of T and
grid (5) of T to +110V, and lowers those of grid (6) of T , and grid (5)
33 36
of T to 46OV: thus
35
^26 grid (3):+7v grid (7):+7v cathode (2) :+7v cathode (8);+7v
grid (3):-29v grid (7):-29v cathode (2):-29v cathode (8):-29v
grid (5):+110v grid (6):+110v cathode (7):+U0v
grid (5):+110v grid (6):+110v cathode (7):+110v
grid (5):+60v grid (6):460v cathode (7) :4^0v
'35
grid (5):460v grid (6):+^0v cathode (7) :+60v
'36
and
T grid (5):-l8v grid (6):-l8v cathode (7):-l8v
22
T grid (5):+7v ffifl (6):-l8v cathode (7) :+7t
23
grid (5) :+7v grid (6):-l8v cathode (7) :+7v
grid (5):+7t grid (6) :+7v cathode (7):+7v
T, grid (5):+8v grid {6)i+8y cathode {l):*&v
4-2
'+3 PTi3 ( -' •. +8v grid (6):-29v cathode (7):+8v

<!-- p. 151 -->
| | grid (5) | grid (6) | cathode (7) |
|---|---|---|---|
| II"" T44 | +8v | -29v | +8v |
| T45 | -29v | -29v | -29v |

the output voltages becoming:

| | | | |
|---|---|---|---|
| To R1 Clear Selector: | +8v | Red Gate: | +7v |
| III"" To R1 Clear Selector: | -18v | Black Gate: | +7v |
| To R2 Clear Selector: | +8v | Green Gate: | +8v |
| To R2 Clear Selector: | -18v | Yellow Gate: | +8v |

Hence, a Yellow or Green Clear is made possible: which is to be performed
is determined by the R1 Clear Selector, which is controlled by the "multiply/
divide" toggle. We also observe that the state of the supertoggle remains
unchanged, since the cathode voltages of T25 and T45 do not change.

We have traced in detail one half cycle of operation of the sequenc-
ing chain. We began with the toggles in chassis 1 and 5 cleared to 1, the
Counter Stop voltage low, and consequently both sections of the supertoggle
tube cut off. This was a stable state of the circuit, which in this condi-
tion permitted no gating or clearing operations to be performed. When the
Counter Stop voltage was raised to its higher value, the supertoggle assumed
its 1 condition. This dropped the voltage output to the R1 and R2 Clear
Selector, which decided, on the basis of the contents of 2^-39 R2, whether to
perform a Black or Red Clear. We assumed that the Black Clear was called for.
The Black Clear being fed back to the Sequencing Chain flipped the toggle in
chassis (1) to 0 which had two consequences: 1) the Black Clear was termin-
ated, and 2) a Yellow Gate was enabled. Again the feeding back of the Yellow
Gate signal flipped the toggle in chassis (5) to 0. This action had again two
consequences: 1) the Yellow Gate was terminated, and 2) the supertoggle was

<!-- p. 152 -->
138.
flipped to 0. This in turn permitted the performance of a Tellow or Green
Clear, depending upon the state of the Multiply/Divide toggle.
If the Bed Clear had been called for, the sequence would have been:
flip the toggle in chassis (5) to 0, terminate the Clear, enable the Oreen
Gate, flip the toggle in chassis (1) to 0, disable the Oreen Gate, flip the
supertoggle to 0.
By continuing the process, we |indj;hat, providing the Tellow Clear
was called for, the signal fed back to the Sequencing Chain flips the tog-
gle in chassis (1) to 1 which terminates the Clear amd enables the Black
Gate. This in turn being fed back flips the toggle in chassis (5) to 1
disables the Black Gate, and flips the supertoggle ageiin to 1. If the
Green Clear is called for, the toggle in chassis (5) is first flipped to 1,
the clear terminated and the Bed Gate enabled. This in turn is fed back to
flip the toggle in chassis (1) to 1, disable the gate, and finally to flip
the supertoggle back to 1.
Thite be'ginni^iig with all three toggles in the 1 condition, first a
Bed or Black Clear is perfonaed followed by a Green or a Tellow Gate, respec-
tively, at the end of which all the toggles are in the condition: this is
one half cycle. The second half cycle begins with a Tellow or Green Clear,
depending upon the axithmetical process to be performed. These are respec-
tively followed by Black or Bed Gates, at the termination of which all the
toggles are again in the 1 condition, and the circuit is ready for another
cycle of operation.
•»
THE DISPATCH CCUWEER
The operation of the Williams Memory requires the i>eriodic regeneration
of the information stored therein. The practical upper bound on the time

<!-- p. 153 -->
139.
batveen regenerations is about one-tenth, of a second; actually it is desir-
able to mabe this Interval shorter, one-thirtieth of a second being satisfac-
tory. The CRT beams must, therefore, be directed in this interval to each
of the memory locations. This requires that in the interval all possible
raenory addresses must be generated and presented to the deflection circuits.
Each memory address is specified by a ten binary digit number, one group of
five digits specifying the Horizontal coordinate; the remaining five the ver-
tical coordinate. Hence, a ten stage binary coxinter which starts at and
counts until all the stages hold I's vill generate in the process all mencry
locations Just once. *'
Furthermore, using as we do a one-address code, ve store orders in
successive locations in the memory and use them in the order in which they
axe stored. There is, however, an exception to this in the case where it
becomes necessazy to shift control, as for example, when it is desired to
repeat a sequence of instructions using new values of the numerical quanti-
ties!
It appears at first glance that the requirements of the Williams
Memory which have been stated above require two counters. However, these
can be combined into a single device which we call the Dispatch Counter.
This is a double counter of the Adder type, consisting physically of three
ranks of ten toggles each and the necessary gate^ clear, and carry circuits.
Each count which anrives at the input causes unity to be added to the lowest
order (2 ) stage and carries to be propagated as appropriate to the higher
order stages.
The three ranks of toggles are referred to as the "restore", "dispatch",
and "order" toggles (Tp, Tj., T.) : the T and T^ toggles form the counter

<!-- p. 154 -->
lito.
which generates the memory addresses for the regeneration process, while the
T and T toggles form the order counter. Im^Aa directly out of the stages
of Tp are taken to the Williams Memory Deflection Generator, while leads into
T make it possible, when it is desired to "shift control", to replace the
I
contents of T by an ao-bitrary number. lajnits are pulses generated in the
D
,*
Williams Memory Local Control: accordiajg as a Regenerate or an Action cycle
is to take place, these are caused to increase the number in T or T by
unity.
The schematic of the Dispatch Counter is shown in DWG No. 1336:two
typical stages are drawn at the left, while the tubes at the right and in
the upper left comer are gate drivers.
Consider a typical stage of tie Counter. The convention here is that
a toggle holds 1 when the left section conducts, as can be seen by the ar-
rangement of the neon lamps. The tube (2C51) directly above T provides the
gates between T and T the left section being the B or "down" gate and
D b', B
the right section the A or "up" gate; the 2C51 directly below T^. provides
ED
the gates between T and T the left section being the A or "down" gate
,
and the right the B or "up" gate. Observe that the B gate guarantees that
B
Tt^, will hold the same bit as T , while clearing T to I's followed by enabl-
ing the B gate guarantees that T will hold the same bit as T • The opera-
tion of tlB A gates will be explained later. The grid voltages of T^ drive
cathode followers; these are both sections of a 2C51. From the cathode of
the left hand section an output is taken to the deflection gates in the
Williams Memory; from each section an output is tapped down slightly below
the cathode. We may assume that the values of these voltages are Ov emd
-UOv for the two states of T . The 6j6 directly above T will be referred

<!-- p. 155 -->
1^1.
to as the carry gate, while the function of the double diode will be ex-
plained below.
The "dispatch" rank of toggles operates together with either the
"restore" or the "order" rank as a true adder. Suppose the number held in
the "restore" rank Is to be increased by unity. The first step is to cleao-
the "dispatch" rank to 0, then to open the BL gates. This puts Into T_ the
number held in T • To this number 1 is added automatically by Introducing
a permanently wired in carry to the lowest order stage. This does not chemge
the state of the T toggles, but sets up the voltages on the grids of the A
gates in such a way that when subsequently T is cleared to I's and the A
B
gates opened, T_ receives a number greater by unity than the one previously
held.
As we saw in studying the Williams Memory local control, the decision
as to whether the next memory cycle is to be one of action or x*egeneratlon Is
made during the X pulse. This decision determines whether unity is to be
added to the contents of T or T The next pulse, "Cl", then performs the
.
R
proper clearing operation in T (the "B clear"), then B is used to open the
B gates. At the beginning of the next cycle, "CI T " clears Tp (or T «is the
case may be) while a pulse coinciding in time with T opens the A gates.
Suppose that unity is to be added to the contents of T,: fhen this
nxunber is read Into T_ by the B gates, and we wish to see how the addition
of unity is effected.
In eadh stage of T we can have either a 1 or a held in the toggle
D
(the Resident Digit), and either a 1 or a as the carry out. This gives us
four cases as shown in the table. In each case we also show the carry from
the preceedlng stage, the carry which must be passed on to the next stage.

<!-- p. 156 -->
the Resident Digit (D_R), and the "new" Resident Digit (D_R'):

| | C in | D_R | C out | D_R' |
|---|---|---|---|---|
| I | 0 | 0 | 0 | 0 |
| II | 0 | 1 | 0 | 1 |
| III | 1 | 0 | 0 | 1 |
| IV | 1 | 1 | 1 | 0 |

As we said before, the "carry" input to the lowest order stage is
permanently wired to a point of negative voltage (-300v), which is the means
used to introduce a 1 into the first stage in the form of an artificial
carry. A carry of 1 is always given by a negative voltage, while a 0 carry
is signified by a positive voltage. In the actual circuit, the lowest
observed 0 carry voltage was +5v, the highest +26v, while the 1 carry volt-
ages ranged from -23v to -27v.

We will now consider in detail each of the four cases for an arbitrary
stage: of course, only cases III and IV can occur in the first stage.

I. The voltage of the right grid of the carry gate is -40v, while
that of the left grid is positive. The cathode, therefore, follows the
left grid high enough to cut off the right section, causing a positive (0)
carry to be transmitted to the next stage. If all the resistors in the
plate network of the right section of the carry gate had exactly their nominal
values, this carry voltage would be +21.4v; the effect of tolerances is such
that values of from +5v to +26v were observed in the ten stages of the counter,
as noted above. The grid of the AR gate would go far negative, but it is held
up by conduction through the left section of the dual diode to about 0v;
measured values of from 0v to +1v were observed.

<!-- p. 157 -->
1>>3.
Next, the T toggle is cleared to 1, and Bubeequently the A gate la
opened by dropping the cathode voltage to -lOv. As the grid voltage of the
A_ gate tube Is Ov, conduction takes place which flips the TL toggle back to
0. Hence, D B' = D B « and C out = 0.
II. Thou^ here the right grid of the carry gate attains a voltage 6f
Ov, the cathode is still held up sxifficiently by the positive volteige of the
left grid that the rl^t section is cut off. Again the carry to the next *
stags is a positive voltage. The left plate of the dual diode la now con-
nected to a point belov ground, vhlle the cathode of the ri^t section is
positive. Hence, the diode is inoperative, and the grid of the A gate
E
—
becomes quite negative from -28v to -31v in the ten stages of the counter.
This suffices to prevent the enabling signal to the A_ g»te from hav-
ing any effect, and, therefore, the T toggle, once cleaa-ed to 1, will remain
B
in that condition. Hence, IL' » 1 and C out = 0.
III. Both grids of the carry gate are negative. We have mentioned that
the highest value of voltage observed for a cairry of 1 is -23v. The right
grid of the T_^ toggle is high (Ov) which permits both diode sections to con-
duct, and thus to hold the carry g^te cathode voltage so high that both sec-
tions are cut off. Hence, we obtain a positive carry voltage to the next
stage, while the A gate grid voltage is observed to lie between -lOv and
-12v.
Thus when the Ap gate is enabled, it does not draw sufficient current
to flip the T toggle from 1, to which it has been cleared, back to 0. Hence,
B
D • » 1, C out = 0.
IV. Here the cathode of the carry gsite follows the rlg^t grid high
enough to cut off the left section, giving a negative (1) carry to the next
^

<!-- p. 158 -->
Ikk.
stage. The grid of the A_ gate la prevented from going poeltlve by
conduction through the rlj^t aectlon of the diode: observed values of
grid voltage range from Ov to -I.5V.
Hence when the A., gate ia enabled, sufficient current Is drawn
to flip Tj^ back to 0, and we have T\^' = 0, C out » 1.
Thus, in the two cases (II and III) In which the "new" digit in
the stage under consideration, resulting from the addition of the carry
from the previous stage to the resident digit, is a 1, the Ap gate grid
voltage is alwa3rs less than -lOv, while in the two caaes (I and IV) in
which it is a 0, the A_ gate grid voltage lies in the range from -l.Jv
to +lv. Thus we see why it is necessary to clear T_ to I's before open-
ing the A- gates; furthermore, it is clear that the Aq gates are kept
closed as long as the cathode voltage is -t-lOv, which is a convenient
level obtained from the Willieuas Memory Local Control. The opening of
the gates can be accomplished by dropping the cathode below the +lv,
-l.^v range. Faster action is obtained the lower the cathode is dropped,
but it is necessary to keep this level sufficiently high that a grid
voltage of -lOv will not result in the drawing of sufficient current to
flip the TL toggle: a lower value of -6v instead of -lOv would appear
to be reasonable here.
TEK MAIN COimiOL QRQAN
In attempting to describe in detail the Main Control Organ of the
mchlne we find it convenient to distinguish first the broad functions it
performs and its over-all interactions both with the subsidiary Memory
and Arithmetic Controls. We intend to proceed in the succeeding pages

<!-- p. 159 -->

![Figure I — Main Control macroscopic inputs/outputs](images/fig_c1.jpg)
*Figure I — Main Control macroscopic inputs/outputs*

Ih'j.
to become more and more detailod about the individual specific func-
tions. Tho text will be accompanied by a number of so-called explan-
atory block diagraiuB, each of which la Intended to reveal some portion
of the functions of the Control. At the end we include a complete
circuit drawing for those readers who ore interested in tracing through
in complete detail the actual physical operation. In the main, however,
we have tried to write our description in a fashion that presupposes
little acquaintance with electronic techniques.
The Main Control viewed macroscoplcally has three inputs and one
output. Two of these inputs are from the Control portion of the Arith-
metic Organ, and the third from the Main Control itself. The output is
connected to the Control portion of the Memory Organ. We Indicate this
below in Figure I.
(-) (O) MLN'ORY Cg) arithmetic!
CONTROL COMTROL I [ CONTROL
i I !
(E)| ifF) (H)| \(J)
AR!THME.TlC|
(e>j MLMOCY
T '
Xc
(A)
G
Tigure I
The reader should view this figure with certain cautions. Since
the principal function of this control is to execute certain orders, its
input is to be viewed primarily as that one labelled (A) . This is the

<!-- p. 160 -->
. .
11*6
one which conveye to the Control the digits expreaslng the order now to
be executed. Obviously this input changes as new orders are to be i>er-
formsd
Each order-word contains actually two distinct orders each of 20
binary digits. This order-word, as we shall see, is placed in H Just
prior to being used. The kO flip-flops in R are symbolized as the single
input (a) above. VHien both pieces of this order-word have been executed
the Main Control generates a new signal or pseudo-order which appears on
input (B) and causes the next order-word to be brought into R.. Normally
this next order-word is that one whose Memory location is one greater
than the one Just executed. This Is not necessarily the case if a trans-
fer of the Control has intervened. (Cf. p. 152.)
The third input (C) to the Main Control is used to notify that
unit that the order under consideration has been executed and that either
inputs (a) or (B) should be examined for the next order.
Before proceeding we describe the temporal order of events at this
point. Clearly since the machine executes orders one after the other
there is a certain cycling nature to the timing. We agree that a period
of time T is begun by the initiation of (A) or (B) and terminated by the
initiation of a signal on (C) . (The periods of time are not necessarily
of equal length but this detail is not yet relevamt.) This termination
can occur only after a number of other events have been completed. Spe-
cifically a signal (D) is sent to the Memory Control; it initiates an
activity in the Memory by a signal (E) which terminates by a signal (F)
to the Memory Control; this latter unit emits a termination signal (3)
which serves to initiate an activity in the Arithmetic Control; this

<!-- p. 161 -->
.
1U7.
control initiates Arithmetic activities (say, an addition operation) by
a signal (H) and receives a notification of completion signal (j) which
serves to generate the final signal (C)
The time order indicated above is dictated by the nature of the
machineb orders. In general, each order requires the specification of
a Memory location and of an operation, one of the operands being stored
in the Memory location. Thus it is natural that the Memory phase of
the Control's activities should precede its Arithmetic phase.
In the block diagram Just discussed above we gave a very general
account of the operation of the Main Control. We wish now to look in
somewhat more detail at some aspects. In peirticular, we shall assume
that an order-word is now in B and that a peurticular half has been
selected for execution. This order contains a digit which specifies
whether the Memory is to be used in the execution of this order, i.e.
it is one of orders 1 - 19, or is not to be used, i.e. it is one of
orders 20-23- In the former case a signal II.D la emitted to the
Willlana Control and in the latter a signal II.D'. (Cf. Figs. I above
and II below.) I.e., the input I.D in Fig. I is in reality two separ-
ate inputs, II.D, II.D'. In either case the Memory Control sends back
to the Main Control an acknowledgment signal 11.10.
As we saw earlier the Memory system is a synchronous one whereas
the rest of the machine is asynchronous. Thus the signal II.D may be
emitted at any given phase relative to the Memory cycle. The Memory
moat necessarily make use of this signal only at a fixed phase in its '
own cycle and must therefore cause the Main Control to delay all other

<!-- p. 162 -->

![Figure II — Williams / Non-Williams Control](images/fig_c2.jpg)
*Figure II — Williams / Non-Williams Control*

<!-- p. 163 -->
1U9.
Wo proceed now to dlBcuas the broad uses of II. and II.0'.
To this end we continue to assuwB we are executlnps a particular order
in R^. The order in question contains a digit which specifies whether
the operation to be performed is arithmetically "trivial", orders 13 -
l8, or is "non-trivial" J orders 1-12. In the former case the Arith-
metic phase of the Control's activities is of essentially zero duration.
We do not need to discuss the signal II.G' in this case since every
order either is non-trivial or makes reference to the Memory. In th«
case of transfer of Control orders, 15 - l8, the signal II. is directly
converted into the termination signal III.C In the case of the store
orders, 13 - 1**, III.C immediately follows the termination of signal
11.10 (time tg in Fig. VIII).
We turn attention now to the non-trivial orders. To this end we
must weiko mention of the so-called Shift Counter. This is a unit of
the Main Control mde necesecury by the inclusion of the multiplication
and division orders. Its main function is to keep count of the various
•teps involved in these operations. It has an input from the Arithmetic
Uinit III.J; and input III.12 which sets up the required count; this may
be implicit as in the case of the multiplication and division orders or
explicit as in the case of the shift orders. It has a single output
III.13 which becomes III.C
There is a unit of the Main Control called the "Oate Clear Se-
quencing Chain" which controls the gating and clearing function* of
registers RI and RII- It is able under the direction of the Arith-
«Btic Control to decide the sequence of gates and clears to apply,
e.g. the sequence for a ri§^t shift, and in addition it controls the

<!-- p. 164 -->

![Figure III — Gate-Clear Chain and Shift Counter](images/fig_c3.jpg)
*Figure III — Gate-Clear Chain and Shift Counter*

<!-- p. 165 -->
digit address and converts it into appropriate deflection voltages for
the Memory cathode-ray tubes. The Order Counter is that unit which
stores a given 10 digit address. This address is one more than the
address from which the order came. It counts modulo 1024.

![Figure IV](images/fig_c4.jpg)
*Figure IV*

We see from Figure IV that both the Main Control and the Order
Counter are capable of feeding information to the Address Generator.
(We use the symbol => to mean mani-fold connections. In this case
10-fold. The Memory output is, of course, 40-fold. The symbol with
several inputs is to mean a gate or set of gates which respond
when and only when both inputs are energized.) The decision as to
which information gets to the Address Generator is determined by a
three stage counter. This counter decides whether the left half L
of an order-word is to be executed, whether the right half R is to be
or whether both have been used and a new order-word obtained.

We see that both the Order Counter and the Main Control itself
can feed address information to the Address Generator. The address
digits of Main Control normally feeds to the Address Generator to

<!-- p. 166 -->
Ij2-
specify the Memory location of the number to bo operated on la the
Arithmetic Unit, 'nhsn, however, both the left- and right-hand halves
of an order-word have been executed the three stage counter advances
to F -- we deacribo on page l6l how this counter is oporatod -- the
address information coming from the Main Control is blocked off and
that from the Order Counter is permitted to enter the Address Generator.
In this fashion the Memory location of the next order la axwclfied.
The stimulus IV.S is used to specify the exact time in the Memory
cycle at which a new address can enter the Address Generator. IV.F la
the aticiulus which specifies that the Memory contents of the Address
in question have been transferred to the Arithmetic Unit --in case of
a store order the flow of information is, of course, reversed. Thus
IV.F becomBS IV.G.«
We remark that the three stage counter is essentially a ring. It
also has certain additional features which are needed to enable trans-
fers of the Control to either the left- or right-hand half of the new
order-word to be effected.
At this point it is convenient to describe the operation of trajis-
ferring the Control, Orders I5 - 18. To do this we must show in more
detail the construction and interrelations Indicated in the previous
drawing. We do this in Figure V below. '

<!-- p. 167 -->

![Figure V — Details of Transfer of Control Orders](images/fig_c5.jpg)
*Figure V — Details of Transfer of Control Orders*

<!-- p. 168 -->
•
I^J*.
effect a transfer of the Control.
Before i'roceedlng, ve diacuss the Disiiatch Ccunter. It consieta
of a Eegeneration Counter vhich ie uaed in connection with tee "refreHh-
ing" of the Heaory's contents and vhich is irrelerar;t in thia diacoaBlooJ
the AddrosB Generator and the Order Counter. Actuaiiy these units are
not completely independent hut are interconnected in the following way:
three registers are used, one directly connected to the Deflection Gen-
erator, the contents of vhich dvtemlne at all tiraes the location of the
electron beam in the memory tubes; another to store the address of the
next point to be regenerated; the third to store the address of the next
order to be brought into BUI. Associated vith the first register is an
adder circuit with one of its inputs always a 1. The output of this
adder peases through gates into the second or third register. In Fig. 1
ve have not shovn the regeneration register.
It is clear from the figure that vhen the toggle F is in the
state F(l) the stinuilus G is passed throu^ the appropriate gate and
becoiaes the so-called "Memory to B. Gate" vhich transfeia the address
location in the Address Generator augnented by 1 into the Order Register.
Furthermore, this same signal, suitably delayed, is used to reset T.
We proceed now to show in considerably sore detail how these
orders vhich make reference to the Meaory, orders 1 - 19, are handled.
This is done in Figxire VI.
To describe the events Indicated in the figure let us suppose
the three state counter la in state L or B. Then the ^tea G.l, G.2
or G.3, G.^ are enabled. Thus the operation portion of either the
left- or ri^t-hand order is permitted to enter the order interpreter.

<!-- p. 169 -->

![Figure VI — Memory Orders](images/fig_c6.jpg)
*Figure VI — Memory Orders*

<!-- p. 170 -->
156.
which ve describe on page l6U> Moreover, the address portion tries
to reach the Address Qenerator. It is blocked by the thresh-hold 3
gate Indicated, until a stimulus leaves the Memory Control. The
Order Interpreter issues a signal called "yea Williams" in Figure VI
and called D in Figure I \^iich will at the beginning of the Memory
phase of the Control's activity be permitted to pass into the Memory
Control. This channel is controlled by the toggle Ty/o which is set
to the zero state by the termination signal of the Control activity.
The Memory Control then issues a pulse called "up" in Figure VI and
11.10 in Figure II.which performs several functions. It puts Ty/o
into the state 1 thereby disabling the communication channel between
the (2>rder Interpreter and the Memory Control; it permits the address
portion of the order being inspected to go to the Address Qenerator;
finally in case the order is a transfer of the Control then it permits
the stinulus T.C, transfer the Control, to set the toggle T^^ into the
1 state.
Then the Memory Control issues a pulse called I which also per-
forms several functions, which are concerned with the toggle T. If
:
1 L is in the state, then I. t produces the so-called Memory to R' gate
and in the contrary case the Memory to B^ Oate. The former case is
associated with the arithmetic operations and the latter with fetching
a new order-word. When the operation of bringing in a new order-word
is being executed, i.e. when the state F(l) or transfer of the Control
obtains then the gating of the order-word into E- (M --> B- Qate) com-
pletes the order. Accordingly after a suitable delay T^^ is returned to
the state by the M --> S^ Gate. Also this gate pulse is used to store

<!-- p. 171 -->
157.
In the Order Baglater the next address after that of the order-word
Just brought into R-.
When the M --> R3 Gate la issued the Memory phase 1b complete
and the Arithmetic phase can begin. Prior to this event the signal
not-Up, Up; has Impressed on the address recognition gates the re-
quired nuBber of shifts for the operation in question, e.g. 2 for
the additive orders, ko for the multiplication, 39 for the division.
Next after a suitable delay -- equal to the duration of the M --> B
Gate -- the M -->R Gate starts the Clear Gate Chain to oi>erate. This
unit has already been instructed as to its functions by the Order
Interpreter, i.e. to shift right or loft or a combination of these.
The Clear Gate Chain in turn coimnands the appropriate clears and
gates in BI and possibly BlI. The execution of these in RI is sig-
nalled back to the Shift Counter. This unit then queries the Address
Recognition Oetes as to whether the current shift count is equal to
that called for by the Order Interpreter. When equality first occurs,
the Recognition Gates issue a stop signal which stops the Clear Gate
Chain and then brings about the termination of the order in that it
causes Ty/o to be reset and the three state counter to be advanced to
the next state.
The.case in which the three stage counter la in the state P(i)
has previously been indicated on page 152 above. We auaaarize here
what occurs. When tills case occurs both halves of the existing order-
word in R, have been executed and therefore Q.l, ..., G.^^ are disabled.
It is desired to bring a new ord^r-word into R- to replace this one.
This is the immediate successor of the order Just executed. Therefore,

<!-- p. 172 -->

![Figure VII — Non-Memory Orders](images/fig_c7.jpg)
*Figure VII — Non-Memory Orders*

<!-- p. 173 -->
.
159.
stlraulua also cauaoB the address portion of the order in queetlon to
be received by the Address Recognition Gates. In all these orders the
Shift Counter autonatically will count up to the Address presented to
these gates. This is in contrast to all Williana orders where the
shift count is specified by the Order Interpreter. The B --> R-^ Gate
from the Non-Williams Control is analogous to the M --> R Gate in that
it starts the Clear Gate Chain, which in turn controls the operations of
RI, RII. As in the Villiama case a signal from RI advances the Shift
Counter; and when the terminal count is reached the Clear Gate Chain is
turned, off.
3
Note that the contents of R are always transferred to B at the
beginning of a Non-Willicuns order. In case of orders 20 - 22, this
transfer is Irrelevant but harmless; the function of the Gate is here
only to start the Clear Gate Chain. But in the case of order RII to
RI, the data are fed into RI via R 3 This arrangemant permits the
.
BII to RI order to have all the variants of orders 1-8, the Addition
Orders
The reader will find in pp. 113 ff detailed expositions of the
•
functions and operations of the Shift Counter, Address Recognition
Gates and the Clear Gate Chain. We accordingly make no further refer-
ences to these units. Instead we take up the three stage counter and
consider it in some more detail. To do this we first indicate the time
relations between the stimuli previously called Up and up (Cf Figure
.
VI).

<!-- p. 174 -->

![Figure VIII — Timing relations for trivial/non-trivial orders](images/fig_c8.jpg)
*Figure VIII — Timing relations for trivial/non-trivial orders*

<!-- p. 175 -->

![Figure IX — Three-stage counter detail](images/fig_c9.jpg)
*Figure IX — Three-stage counter detail*

<!-- p. 176 -->

![Figure X — Non-Williams Control (R2 to R3 transfer)](images/fig_c10.jpg)
*Figure X — Non-Williams Control (R2 to R3 transfer)*

<!-- p. 177 -->

![Figure XI — RII Load order control](images/fig_c11.jpg)
*Figure XI — RII Load order control*

<!-- p. 178 -->
![Gate notation symbol](images/fig_c_gatesymbol.jpg)

is understood to mean this: A signal appears at (3) if and only if
one appears at (2) but none appears at (1). In terms of this we
see that the transfer from R3 to R2 is not permitted until just after
the transfer from the Memory to R3.

We next show in Figure XII the Order Interpreter. The presenta-
tion is in terms of dichotomies determined by the order digits in ap-
proximate time sequence of choice. Each digit of the order is con-
sidered as having a "0" state or a "1" state. In the diagram the
digit, expressed as 0 --- 9 corresponding to positions 10 - 19 or
30 - 39 depending on the order phase, is denoted by the number enclosed
in a circle. The "1" choice corresponding to this digit is always the
right branch; the "0" choice is always the left. Specific orders result-
ing from the various digit possibilities are denoted by their list
number enclosed in a square.

A few special remarks: the internal orders, determined by
D1 = 1, are initiated by the state of D2 being either "0" or "1" as
distinct from "off". The necessity for this feature may be verified
by observing that R3 contains two orders of which one must be selected
by turning its gates "on" and the other necessarily has its gates "off".
Again, in the change from an old order to a new one, a period must
intervene in which the changing order is, as seen by the Main Control,
"off", and it is essential that this "off" state be unable to initiate
any Main Control activities.

<!-- p. 179 -->

![Figure XII — Block Diagram of Order Interpretation](images/fig_c12.jpg)
*Figure XII — Block Diagram of Order Interpretation*

<!-- p. 180 -->
166.
Alao, not all digits are represented on this dle,2ram. As an
ezaraple, the magnitude/number digit, D. enters only into the setting of
the Complement Gates and has no direct effect on order timing. Simi-
larly the minus left/plus right digit, D^i in the case of summation
orders affects only the Complement Qatee and again doea not determine
a true dichotomy in time.
Finally, the terminal process to an order is usually the "step"
to the next order. For most orders this "step" may be auppressed and
computation stopped by setting the step digit, D,^, to a "0". This
final choice of step or stop is not shovn on the diagram.

<!-- p. 181 -->
*(This final page is the library's inside-back-cover catalog card —
Institute for Advanced Study, Math. & Nat. Sci. Library, Princeton, N.J. —
not part of the report's content.)*