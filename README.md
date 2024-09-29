# Python Binary Converter

This is a pretty simple binary converter, it only runs on terminal, so I didn't used any library to this project, except for:
 * Platform: used to get the user operational system;
 * OS: to make some commands on the command prompt;
 * Time: to wait some time before the code keeps running.

I had the idea of doing that code after a class in my technician IT course where my teacher told us how to convert binary codes.

---

# Index  
* [Introduction](#intro)
* [Counting Systems](#CountingSystems)  
* [Binary to Decimal Logic](#BToD)
* [Decimal to Binary](#DToB)
* [My Code (Binary to Decimal](#myCode1)
* [My Code (Decimal to Binary](#myCode2)
* [Thanks for reading](#thx)

# <h1 id ="CountingSystems">Introduction</h1>

That's a brief explanation and deducing of how to do those calculus, so if you want to get into all the mathematic nuances of everything I recommend reading the websites:
* CueMath - [Binary To Decimal](https://www.cuemath.com/numbers/binary-to-decimal/);
* CueMath - [Decimal to Binary](https://www.cuemath.com/numbers/decimal-to-binary/).

Anyways, lets get into all that nerdy stuff!

---

# <h1 id ="CountingSystems">Counting Systems</h1>

With that said, here it goes the explanation of all the logic. For starting, you need to know what is decimal or binary.

In math studies we have different types of counting systems, they differ from each other by how many numbers you need to count to add another number to the next digit. So basically, in the decimal system you need to count ```10``` numbers to add another number to the left. Therefore, you count ```0, 1, 2, 3, 4, 5, 6, 7, 8, 9``` and only then you add a number ```1``` to the left to get a ```10``` and start counting again, until you pass for all ```10, ... , 20 ... , 30 ... , 40 ... , 50 ... , 60 ... , 70 ... , 80 ... , 90 ... , 99``` to finally add another digit to the number to get ```100```. 

It's similar of counting on your fingers, you mark how many ```10```'s you've count and at the end you just multiply by ten to get how many numbers you had counted.

The hexadecimal system follows the same logic, but, instead of adding ```10``` numbers, as you can tell, it adds ```16``` "numbers". But we have only ```10``` numbers, so when you want to represent ```10, 11, 12, 13, 14, 15 or 16``` in hexadecimal you can just use the letters ```A, B, C, D, E, or F``` respectively.

However, the binary system is different, instead of using ```10``` or ```16``` symbols to start counting again, you use only ```2``` numbers, ```0``` and ```1```. So to represent the number ```0``` in binary, you can only put ```0```, and to represent ```1``` you put ```1```.

But now, to represent ```2``` you have to put another ```1``` on the left and start counting again, the same way we do in all counting systems. So the number ```2``` in binary is represented by ```10```. BTW The numbers in binary are spelled like "one, zero" not "ten", because if you say "ten", is implicit that you're talking about a decimal number.

----

# <h1 id ='BToD'>Deducing the Binary to Decimal logic</h1>

Having that said, we can infer that every time you add a digit to a Binary number you are adding a exponent of base ```2```, so in the first position you have a ```1```, you can multiply that ```1``` to ```2 ^ 0```, id est ```1 . 2 ^ 0```. Every number elevated to the power ```0``` equals to ```1```, so the number ```(1)10``` is represented by the number ```(1)2```.

What if we want to translate ```(1010)2``` to decimal? We can do the same thing as before, but now we have to add every number resulted by the calculation of the 2 exponents. So you have:

```(0 . 2 ^ 0) + (1 . 2 ^ 1) + (0 . 2 ^ 2) + (1 . 2 ^ 3)```

If you sum all that stuff, you end up with:

```0 + 2 + 0 + 8```

Which is simply ```10```.

And then you can ensure that the number ```(1010)2``` is ```(10)10```.


# <h1 id ="DToB">Deducing the Decimal to Binary logic</h1>

This logic is simpler, the only thing you need to understand is that the binary number is equal to the decimal divided by ```2```, and you get the remainder of that division. You do it until you cannot divide it anymore. So then you take all the numbers of the remainder in the multiplication and organize then in the opposite direction.

For example, the number ```10```, you divide it until you cannot anymore:

```10 / 2 = 5 ``` and ```remainder = 0```

```5 / 2 = 2``` and ```remainder = 1```

```2 / 2 = 1``` and ```remainder = 0```

Now that you can't divide it anymore, you just put the result of the last division (which is 1) and rearrange the remainders in the opposite direction like: ```1010```. And that's it, now you know that ```(10)10``` is equal to ```(1010)2```.

---


That's all you need to know to understand what I've done on my code, so lets dive right into that!!!



---

# <h1 id ="myCode1">My Code (Decimal to Binary):</h1> 

Skipping all lines that are system functionalities, we can jump into the method "binaryToDecimal". This method starts getting an ```Array``` of ```Strings``` typed by the user, so if you type ```1010```, the code will interpret it as if it was ```['1', '0', '1', '0']``` and finally it puts it inside the variable ```binary```.

![image](https://github.com/user-attachments/assets/6f60b3a0-1853-4364-b8f2-662a39dd95b7)



To continue with the calculus, the code then invert the order of the ```Array```, you will see for what I've done that.

![image](https://github.com/user-attachments/assets/3b114fee-80a2-4fde-ab80-0a4512780ee2)

After all this, the code then get into a ```for loop``` that repeat the same amount of the length of the ```Array binary```. This loop basically gets the position in the array and set the value of that position equals to the product of the multiplication of the original number by two to the zeroth power. This sounds hard to understand but the image explains it simpler:

![image](https://github.com/user-attachments/assets/d244d5d3-27ad-48b8-8338-e9df67efe3eb)

And thats it, you got all logic for converting decimal to binary!!! Now, here it goes the logic to convert Binary to Decimal.

---

# <h1 id ="myCode2">My Code (Binary to Decimal):</h1>
In that section, I just made a ```decimal``` variable that stores the decimal number. After that I put a backup variable ```n1``` for the value of the decimal, and a ```n2``` that makes the same thing. I started a ```remainder_str``` to put all remainders together, and finally a ```remainder``` that will store the remainder for each division (```while loop```).

![image](https://github.com/user-attachments/assets/defd4f65-d903-4fa1-beb0-2e26b9fa961a)

After that, I started a while loop that goes until the value of ```n1``` equals 1. So it will repeat until it's impossible to divide the number by 2. This loop stores the remainder of the division in the ```remainder```variable. Divide ```n1``` by 2 and store the result in the ```n1``` variable. It stores the remainder into the ```remainder_str``` concatenating with the previous result in each loop. Finally the loop update the value of ```decimal``` to the value of ```n1``` variable.

![image](https://github.com/user-attachments/assets/38372365-bdd3-4318-b994-618731477355)

After the loop, the code updates the ```remainder_str``` to concatenate the result of the last division. And it prints the result for the user.

---


# <h1 id ="thx">Thanks for Reading</h1>

Now you have it, that was all the coding for this program. I'm so grateful that you had read this whole archive. I hope so much you enjoyed and got every logic for all coding, thats not a very impressive code or something, but it's always good to make things like that. Anyways, thank you for the prestige and goodbye.
