# Author: Liu Yutong
# Date: 04/06/25
# Description: Quiz with LED feedback

import RPi.GPIO as GPIO
import time

# GPIO 
GPIO.setmode(GPIO.BCM)
GREEN_PIN = 17
RED_PIN = 18
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)

def control_led(pin, duration=1):
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(duration)
	GPIO.output(pin, GPIO.LOW)

def quiz():
	questions = [
		"1. Which is NOT a Python data type?\na) int\nb) float\nc) rational\nd) string\ne) bool",
		"2. Which is NOT a built-in operation?\na) +\nb) %\nc) abs()\nd) sqrt()",
		"3. In mixed-type expressions, Python converts:\na) floats to juts\nb) juts to strings\nc) floats and juts to strings\nd) juts to floats",
		"4. Best structure for multi-way decision?\na) if\nb) if-else\nc) if-elif-else\nd) try",
		"5. Terminate a loop?\na) if\nb) exit\nc) continue\nd) break"
	]
	answers = ["c", "d", "d", "c", "d"]
	score = 0

	for i in range(len(questions)):
		user_answer = input(questions[i] + "\n> ").strip().lower()
		if user_answer == answers[i]:
			print("Correct!")
			control_led(GREEN_PIN)
			score += 1
		else:
			print("Incorrect!")
			control_led(RED_PIN)

	print(f"\nFinal Score: {score}/{len(questions)}")
	GPIO.cleanup()

if __name__ == "__main__":
	quiz()
