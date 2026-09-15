# IAS Machine Documentation - Pages 6 to 20 (Corrected Transcription)

## Page 1 (Original Page 6)
### Fig. I. 1.
```
       ┌────────────────────────┐
       │       Register I       │◄────────┐
       └───────────┬────────────┘         │
                   │                      │
       ┌───────────▼────────────┐         │
       │      Register II       │         │
       └────────────────────────┘         │
                                          │
       ┌────────────────────────┐   ┌─────┴──────┐
       │      Register III      ├──►│   Adder    │
       └────────────────────────┘   └────────────┘
```
**Fig. I. 1.**

As indicated in the figure, the inputs (40-fold in each case) to the Adder are from Registers I and III — we shall use the symbols $R_I$ and $R_{III}$ in the future — and the output of this unit is stored back in $R_I$. Again, information in $R_{III}$ can be communicated to $R_{II}$ and hence to $R_I$ without proceeding through the Adder. In an addition, the augend is originally in $R_I$ and the addend in $R_{III}$, the sum being placed in $R_I$ at the completion of the operation.

To make clear the subtraction, we must make mention of a unit called the **Complement Gate Chassis** which intervenes between $R_{III}$ and the Adder, as indicated in the figure below.

```
                         ┌───────────────────────┐
                         │ Complement Correction │
                         └───────────┬───────────┘
                                     │
                                     ▼
┌──────────────┐   ┌─────────────────┴─┐   ┌───────────┐
│    R III     ├──►│ Complement Gates  ├──►│   Adder   │
└──────────────┘   └───────────────────┘   └───────────┘
```
**Fig. I. 2.**

---

## Page 2 (Original Page 7)
This chassis permits one of three modes of communication between $R_{III}$ and the Adder. If a number $x$ is stored in $R_{III}$, then either the Complement Gates permit $x$, the complement of $x$, or $0$ to enter the Adder; or, to be more precise, if $x = (x_0, x_1, \dots, x_{39})$, then either $x$ or $(1-x_0, 1-x_1, \dots, 1-x_{39})$ or $0 = (0, 0, \dots, 0)$ is permitted to enter the Adder from $R_{III}$. If it is the middle case, then the Arithmetic Control also "injects" a digit $2^{-39}$ into the Adder. This, as we shall see, correctly handles the operation of subtraction.

To form $x - y$, we proceed as follows: the Arithmetic Organ has $x$ in $R_I$, $y$ in $R_{III}$ and has been instructed to form the difference. It forms, apart from the "complement correction" just mentioned,
$$\sum_{i=0}^{39} (x_i + (1 - y_i)) \cdot 2^{-i} = x + (2 - y) - 2^{-39}$$
The complement correction then has the effect of removing this last $2^{-39}$ and yielding the correct difference.

We leave this discussion of the separate units of the Arithmetic Organ for the moment but with the intention of returning to it shortly.

The multiplication operation is somewhat more delicate in a certain sense than are the addition and subtraction because the procedure based on the modulo 2 fails completely. If one changes one factor, say $x$, of a product $xy$ by a two, then the new product differs from $xy$ by $2y$ which is not generally an integer multiple of 2 since $-1 \le y < +1$.

To effect a multiplication we store the multiplier in $R_{II}$ and the multiplicand in $R_{III}$. We carry out the process by seriatim multiplying the entire multiplicand by the digits of the multiplier starting with the least significant one.

---

## Page 3 (Original Page 8)
The multiplication proper takes place in 39 steps, corresponding to the 39 non-sign digits of the multiplier, together with several "clean-up" operations in addition. We describe all this below. For simplicity we first consider the case in which both the multiplier $x = (x_0, x_1, \dots, x_{39})$ and the multiplicand $y = (y_0, y_1, \dots, y_{39})$, i.e., $x_0 = y_0 = 0$ and hence $0 \le x < 1, 0 \le y < 1$.

Assume we have already performed the first $i - 1$ steps of the multiplication involving the multiplication of the multiplicand by the last $i - 1$ digits of the multiplier, $x_{39}, x_{38}, \dots, x_{41-i}$. We describe now the multiplication with the $i$-th digit, i.e., with $x_{40-i}$. Assume that $R_I$ contains the partial product after the last step, $p_{i-1}$ (for $i = 1, p_0 = 0$). We form
$$2p_i = p_{i-1} + y_k \quad 	ext{with} \quad y_k = egin{cases} 0 & 	ext{for } x_{40-i} = 0 \ y & 	ext{for } x_{40-i} = 1 \end{cases}$$
I.e., if $x_{40-i} = 0$ we define $p_i$ as $1/2$ of $p_{i-1}$ and if $x_{40-i} = 1$ as $1/2$ of $(p_{i-1} + y)$. Consider now the sizes of the quantities $2p_i$. For $i = 0$, $0 \le 2p_i < 2$ (since $p_0 = 0$); now if this is true for $i - 1$, then our displayed definition above makes it also true for $i$. Thus $2p_i$ lies in the interval $0 \le 2p_i < 2$ and no carry can arise beyond the $2^0$-position.

Thus $p_i$ is formed from $2p_i$ by a right shift with the sign digit made 0. Finally we have
$$p_{39} = 2^{-1}(2^{-1}(2^{-1}(\dots(2^{-1} x_{39} y + x_{38} y)\dots)+ x_2 y) + x_1 y) = \sum_{i=1}^{39} 2^{-i} x_i y = xy$$
i.e., we have our correct product. We describe later how we achieve this in the Arithmetic Organ. At the moment, however, we turn instead to the

---

## Page 4 (Original Page 9)
other possible cases, namely: $x < 0, y \ge 0$; $x < 0, y < 0$; $x \ge 0, y < 0$.

We pass now to these cases and describe how they are performed.

If $x < 0$, then it is represented in the machine as $x + 2$. Thus for $x < 0, y \ge 0$ the procedure we have just described would form not $xy$ but $xy + 2y$; for $x < 0, y < 0$ it would form $xy + 2x + 2y + 4$; for $x \ge 0, y < 0$ it would form $xy + 2x$. Hence, correction terms $2x, 2y$ or both would be needed. As we shall see later these corrections would be quite awkward for us to perform, particularly the correction $2x$ since we in fact lose the digits of the multiplier as they are no longer needed. The reason for this will become apparent in the next section.

Our procedure is this: First let us assume that the corrections necessitated by $y < 0$ have been disposed of and permit $y to be either $\le 0$ or $> 0$. We focus attention now on $x < 0$.

We disregard the sign digit of $x$ and act as if it were 0. Then $x$ is replaced by $x^1 = x - 1$ but since $-1 \le x < 0$, $x^1$ will act as if it were $(x - 1) + 2$. Hence our procedure for multiplication will produce $x^1 y = (x + 1) y = xy + y$. We therefore need a final correction in this case of $-y$ at the end of the process. Thus in the cases $x < 0$ we proceed through the 39 steps described earlier and thereby form $xy + y$ and then we must perform another step to subtract out the multiplicand $y$.

Having disposed of the difficulties that arise when $x < 0$, we may now assume $x \ge 0$ and consider the one remaining case, namely $y < 0$.

Suppose this time that we ignore completely the sign digit of $y$, or rather that we replace it by 0. Then if $y^1 = y - 1$, we have as before $xy^1 = x(y + 1) = xy + x$ and a correction $-x$ is needed. Since, however,

---

## Page 5 (Original Page 10)
we do not have $x$, the multiplier, available at the end of the multiplication we must find a means of applying this correction as the first 39 steps proceed. We proceed in this fashion: when we examine the digit $x_{39-i}$ of the multiplier, we normally add into the partial product $p_i$ the number $y$ if $x_{39-i} = 1$ and 0 otherwise. Let us now modify this procedure as follows:
$$2p_i = p_{i-1} + \hat{y}_i \quad 	ext{with} \quad \hat{y}_i = egin{cases} 1 & 	ext{for } x_{40-i} = 0 \ y^1 & 	ext{for } x_{40-i} = 1 \end{cases}$$
As before $0 \le 2p_i < 2$ and no carries can proceed beyond the $2^0$-position. Let us see now what result we have produced by this procedure.
$$p_{39} = 2^{-1}(2^{-1}(2^{-1}(\dots(2^{-1}x_{39}y^1 + 2^{-1}(1-x_{39}) + x_{38}y^1 + (1-x_{38}))\dots) + x_2y^1 + (1-x_2)) + x_1y^1 + (1-x_1) =$$
$$= \sum_{i=1}^{39} 2^{-i} x_i y^1 + \sum_{i=1}^{39} 2^{-i}(1 - x_i) = xy^1 + 1 - 2^{-39} - x =$$
$$= x(y+1) + 1 - 2^{-39} - x = xy + (1 - 2^{-39})$$
Thus a final correction of $-1 + 2^{-39}$ is necessary. But this correction which is done at the end can be effected modulo 2 and we can correct it by $1 + 2^{-39}$.

We summarize now in a general description covering all four cases.

We return now to our schematic discussion of the Arithmetic Organ. Since we wish to retain the full 78 digits of a product, we have established certain interconnections between $R_I$ and $R_{II}$ not yet shown in Figure I.1. Before describing them we must indicate another feature of $R_I$ and $R_{II}$. Each of them is capable not only of receiving 40 digit

---

## Page 6 (Original Page 11)
numbers and of transmitting them, but also of translating either to the right or left whatever information is stored in them. We discuss the logical implications of these shift facilities later. At the moment we prefer to indicate how this is accomplished, at least in a crude way.

Each of $R_I$ and $R_{II}$ is in reality not one but two registers suitably interconnected. Let us consider $R_I$ first. It consists of two registers and four sets of 40-fold gates. Let the two registers be denoted by $R^I$ and $R_I$. One set of gates intervenes between the Adder and $R^I$. Thus the output of the Adder is stored at least initially in $R^I$. Two sets of gates allow communication from $R^I$ to $R_I$ and a fourth set allows communication from $R_I$ to $R^I$.

The set which controls the communication between the Adder and $R^I$, the so-called Green Gates, is so wired that it makes digital position $2^{-i}$ of the Adder correspond to $2^{-i}$ of $R^I$. One of the two sets controlling the route from $R^I$ to $R_I$, the so-called Red Gates, makes position $2^{-i}$ of $R^I$ correspond to $2^{-(i-1)}$ of $R_I$; the other set, the so-called Black Gate, makes $2^{-i}$ of $R^I$ correspond to $2^{-(i+1)}$ of $R_I$. The fourth set, the so-called Yellow Gate, from $R_I$ to $R^I$ makes $2^{-i}$ of $R_I$ correspond to $2^{-i}$ of $R^I$. We indicate this below in Figure I.3.

A similar arrangement obtains with respect to $R_{II}$. The structure of $R_{III}$ is, however, simpler since it is not called upon to perform shifting functions as are $R_I$ and $R_{II}$.

---

## Page 7 (Original Page 12)
### Figure I. 3.
```
                   ┌───────────────┐
                   │     Adder     │
                   └───────┬───────┘
                           │ Green Gate
                           ▼
                   ┌───────────────┐
                   │      R^I      │
                   └─┬───────────┬─┘
        Red Gate     │           │     Black Gate
     ┌───────────────┘           └───────────────┐
     │ (i-1)                                     │ (i+1)
     ▼                                           ▼
┌───────────────┐                         ┌───────────────┐
│     (i-1)     │                         │     (i+1)     │
└───────┬───────┘                         └───────┬───────┘
        │                                         │
        └────────────────┐       ┌────────────────┘
                         │       │
                         ▼       ▼
                   ┌───────────────┐
                   │      R_I      │
                   └───────┬───────┘
                           │ Yellow Gate
                           ▼
                   ┌───────────────┐
                   │   (Transient) │
                   └───────────────┘
```
*(Note: Red Gates route $i 	o i-1$, Black Gates route $i 	o i+1$, and Yellow Gates return data back up to $R^I$.)*

**Figure I. 3.**

We can now describe in somewhat more detail the operations previously alluded to such as the right and left shifts, the transfer into $R_I$, the addition, the subtraction, and at least part of the multiplication.

Consider first a number in $R_I$ — in both $R_I$ and $R_{II}$ the units $R^I, R^{II}$ serve only as transient storage positions; all storage for more than a few microseconds is in $R_I, R_{II}$ — which we desire to shift right (left). The Arithmetic Control routes the information first to $R^I$ via the Yellow Gate set, then back to $R_I$ via the Black (Red) Gate set. (We must describe later treatment of the sign digit.)

Next consider a number arriving in $R_I$ from the Adder. It is transferred to $R^I$ via the Green Gate set, then to $R_I$ via the Red set — note this apparently causes the information in $2^0$-position of the Adder

---

## Page 8 (Original Page 13)
to be lost. Actually it does not because $R_I$ has a $2^{+1}$ position for precisely this reason; it is then sent back to $R^I$ via the Yellow set and finally back to $R_I$ via the Black set. Note that it is now correctly positioned, i.e., the content of $2^{-1}$-position of $R_I$ is that of $2^{-1}$-position of the Adder.

In the next figure we indicate the connections between $R_I$ and the Adder, suppressing the gate sets.

```
       ┌────────────────────────┐
┌─────►│          R^I           │
│      └────────────────────────┘
│
│      ┌────────────────────────┐         ┌───────────────┐
│      │          R_I           ├────────►│     Adder     │◄───── From R_III
│      └────────────────────────┘         └───────┬───────┘
│                                                 │
└─────────────────────────────────────────────────┘
```
**Figure I. 4.**

---

## Page 9 (Original Page 14)
from $R_I$ to $R_{II}$ but not back again. This connection is provided so that whenever a right shift occurs the digits being shifted out of $R_I$ are stored in $R_{II}$. We make this connection quite specific in Figure I.5 below.

```
┌──────────────────┐
│       R_I        ├──┐
└──────────────────┘  │
                      ▼
┌──────────────────┐
│       R_II       │◄─┘
└──────────────────┘
```
**Figure I. 5.**

To provide for the comparable situation when a left shift occurs the $2^0$ stage of $R_I$ is connected to the $2^{-39}$ stage of $R_{II}$, as in Figure I.6 below.

```
┌──────────────────┐
│       R_I        │◄─┐
└──────────────────┘  │
                      │
┌──────────────────┐  │
│       R_II       ├──┘
└──────────────────┘
```
**Figure I. 6.**

We are now able to proceed further with the details of the multiplication. The multiplier is initially placed in $R_{II}$. (This must be done prior to the multiplication order, c.f. 0.9 below.) Then when the multiplication is initiated the multiplicand is in $R_{III}$. An observation post exists at stage 39 of $R_{II}$ which examines whether the digit therein is 0 or 1 and acts accordingly, i.e., it does not or does

---

## Page 10 (Original Page 15)
add the multiplicand into $R_I$ in case both multiplier and multiplicand are positive. We discuss below the exact details in all cases. Then a right shift of one is performed. Thus three things occur of relevance: first, the partial product in $R_I$ is properly positioned for the next step; second, the digit of the multiplier last examined has been lost and the next relevant, i.e., the now currently relevant, is available at the inspection station; third, the least significant digit of the partial product has now been shifted into $R_{II}$, into the leading stage. This procedure is carried on for the 39 steps required at which time the 39 most significant digits of the product appear in $R_I$ and the 39 least significant ones in $R_{II}$.

The addition operation is performed in this fashion: We assume the augend is now in $R_I$, specifically in $R_I$, and the addend is in $R_{III}$. The Complement Gates are set to pass the addend out and the sum is then stored temporarily in $R^I$. This sum is then put into $R_I$ displaced one to the left with the sign digit in $2^{+1}$. Next, the number is transferred back to $R^I$ and thence down to $R_I$ in the correct position. In terms of the various gating operations this means the following: The Green Gates were opened to admit the sum to $R^I$; the Red Gates sent it to $R_I$; the Yellow Gates sent it back to $R^I$; and finally it arrived correctly positioned in $R_I$ via the Black Gates.

The situation for the subtraction differs in one point only; the Complement Gates are opened to pass the complement of the addend and the complement correction is carried out.

In both cases the sign of the sum is now both in $2^{+1}$ and $2^0$.

---

## Page 11 (Original Page 16)
The possible addition and subtraction operations performable by the machine are these:
1. The addition (subtraction) of the contents of $R_{III}$ and of $R_I$.
2. The addition (subtraction) of the contents of $R_{III}$ and of $R_I$ pre-cleared to 0. I.e., the transfer of a number (or its complement) into $R_I$.
3. The addition (subtraction) of the absolute value of the contents of $R_{III}$ and of $R_I$.
4. The addition (subtraction) of the absolute value of the contents of $R_{III}$ and of $R_I$ pre-cleared to 0. I.e., the transfer of the modulus of a number (or its complement) into $R_I$.

To perform the operations involving absolute values, the Arithmetic Control is provided with a monitor which decides whether the Complement Gates are to pass the number in $R_{III}$ or its complement according as the instruction requires.

The left shift is performed analogously to that for the right shift but the right-most stage of $R_I$ is made 0.

This is the correct convention to ensure that the left shift is exactly a multiplication by 2 (provided that the result is still in "scale", i.e., is not outside the interval $-1 < x < 1$).

The left shift operation can be performed $n$ times ($1 \le n \le 47$) by means of a single order.

The right shift operation is performed in this fashion: The number in $R_I$ is transferred into $R^I$ and is then sent back into $R_I$ displaced one position to the right. Exactly the same procedure is followed in $R_{II}$.

---

## Page 12 (Original Page 17)
Thus both $R_I$ and $R_{II}$ shift together. (There is one exception to this principle in one of the terminal steps of a multiplication but this need not concern us here.)

The information stored in $2^{+1}$ of $R_I$ is therefore shifted into $2^0$. It is also retained in $2^{+1}$. If this digit is a 0, the sign of the resulting quantity is 0 and if it is a 1, the sign is 1. But this is exactly the correct convention to ensure that the right shift is exactly a division by 2.

The right shift operation can be performed $n$ times ($1 \le n \le 47$) by means of a single order.

This amounts only to an iteration $n$ times of what is described above.

Since $R_I$ and $R_{II}$ are interconnected as shown in Figure I.5 above, the information shifted out of $R_I$ is transferred into $R_{II}$; but the material shifted out of $R_{II}$ is lost.

We next discuss the division operation. To make precise what follows we agree that the dividend is $x$, the divisor is $y$ with $-1 \le x < 1$, $-1 \le y < 1$, $|x| < y$.

To describe the process we assume that the first $i - 1$ steps of the division have been completed and that the first $i - 1$ digits $q_0, q_1, \dots, q_{i-2}$ of the quotient $Q$ are in positions $40-i, 41-i, \dots, 39$, respectively. We also assume that $y$, the divisor, is in $R_{III}$ and that the remainder $r_{i-1}$ is in $R_I$. We proceed inductively in this fashion:
$$(1) \quad r_i = 2r_{i-1} - (	ext{sgn } xy) y p_{i-1}, \quad r_0 = x/2$$
where

---

## Page 13 (Original Page 18)
$$(2) \quad p_{i-1} = egin{cases} 0 & 	ext{sgn } r_{i-1} 
eq 	ext{sgn }(2r_{i-1} - (	ext{sgn } xy) y) \ 1 & 	ext{sgn } r_{i-1} = 	ext{sgn }(2r_{i-1} - (	ext{sgn } xy) y) \end{cases}$$
$$p_0 = 0$$
We next define $q_i$ as
$$(3) \quad q_i = egin{cases} p_i & 	ext{sgn } xy = +1 \ 1 - p_i & 	ext{sgn } xy = -1 \end{cases}$$

We now show that
$$	ext{sgn } r_i = 	ext{sgn } x, \quad |r_i| < |y|$$
We prove these inductively. They are evidently true for $i = 1$. We show they are true for $i + 1$ assuming they are true for $i$. If $	ext{sgn } r_i = 	ext{sgn }(2r_i - (	ext{sgn } xy) \cdot y)$ then $p_i = 1$ and
$$r_{i+1} = 2r_i - (	ext{sgn } xy) \cdot y$$
and
$$	ext{sgn } r_{i+1} = 	ext{sgn } r_i = 	ext{sgn } x$$
Next,
$$2r_i - (	ext{sgn } xy) \cdot y = 2 	ext{sgn } r_i \cdot |r_i| - 	ext{sgn } x \cdot 	ext{sgn } y \cdot y =$$
$$= 2 	ext{sgn } x \cdot |r_i| - 	ext{sgn } x \cdot |y| = 	ext{sgn } x (2 |r_i| - |y|)$$
Thus
$$r_{i+1} = 	ext{sgn } r_{i+1} \cdot |r_{i+1}| = 	ext{sgn } x \cdot |r_{i+1}| = 	ext{sgn } x (2 |r_i| - |y|)$$
and
$$|r_{i+1}| = |2r_i| - |y| < 2|y| - |y| = |y|$$
which completes the induction in this case. In the contrary case $p_i = 0$ and $r_{i+1} = 2r_i$,

---

## Page 14 (Original Page 19)
and
$$	ext{sgn } x = 	ext{sgn } r_i 
eq 	ext{sgn }(2r_i - (	ext{sgn } xy) \cdot y) = 	ext{sgn } x \cdot 	ext{sgn }(2|r_i| - |y|)$$
Thus
$$	ext{sgn }(2|r_i| - |y|) = -1$$
i.e.,
$$|r_{i+1}| = 2|r_i| < |y|$$
and $	ext{sgn } r_{i+1} = 	ext{sgn } 2r_i = 	ext{sgn } r_i = 	ext{sgn } x$, since $2r_i$ is in the machine's number range. Hence we have proved our induction.

We multiply both sides of (1) by $2^{-i+1}$ and sum for $i = 1, 2, \dots, n$. We find
$$2^{-(n-1)} r_n = 2^1 r_0 - (	ext{sgn } xy) y P$$
where
$$P = \sum_{i=0}^{n-1} 2^{-i} p_i$$
Thus
$$(4) \quad x = (	ext{sgn } xy) P \cdot y + R$$
where
$$R = 2^{-n+1} r_n$$
since $2^1 r_0 = x$.

If $	ext{sgn } xy = +1$, (4) becomes with the help of (3)
$$x = Q y + R$$
where
$$Q = \sum_{i=0}^{n-1} 2^{-i} q_i = P$$

If $	ext{sgn } xy = -1$, then
$$Q = \sum_{i=0}^{n-1} 2^{-i} q_i = \sum_{i=0}^{n-1} 2^{-i}(1 - p_i) = 2 - 2^{-n+1} - P$$

---

## Page 15 (Original Page 20)
i.e., apart from the term $2^{-(n-1)}$, $Q$ is the complement of $P$. Thus our quotient is wrong in the last place.

Up to this point we have made no mention of "rounding" procedures. We do not wish in this place to discuss the theoretical background of such procedures. Instead we merely call the reader's attention to such a discussion in a previous report $^1$ and state the rules we have adapted. In the multiplication operation a digit is added to $2^{-40}$ and the result truncated after 39 digits after all carries have been completed. In the division operation we perform 39 steps determining the sign and 38 information digits. The 39th such digit is automatically made 1.

We complete our discussion with a discussion of the roles of $R_I, R_{II}, R_{III}$ during the division operation.

At the start of this operation the dividend is in $R_I$, the divisor is in $R_{III}$. Although left shifts are to be performed, the channel from $R_I$ to $R_{II}$ which normally transmits for a left shift is suppressed. Instead the quotient digits are inserted seriatim into position 38 of $R_{II}$ and shifted left. The operation continues until the sign digit of the quotient reaches position 0 of $R_{II}$. At this time the remainder is in $R_I$.

It remains only to explain how the machine makes the discriminations indicated in (2), (3) above. First we note that in (2) the expression "	ext{sgn } r_{i-1}" can be replaced by 	ext{sgn } x. Thus (2) becomes

---
1) *Preliminary Discussion of the Logical Design of an Electronic Computing Instrument*, Burks, Goldstine and von Neumann, Pt. I, Vol. I, 1946, pp. 19, ff.
