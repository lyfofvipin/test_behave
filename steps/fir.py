# import sys, pdb; pdb.Pdb(stdout=sys.__stdout__).set_trace()
from behave import Given, When, Then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from time import sleep

@Given("Simple function {xyz}")
def simp(context, xyz):
	context.execute_steps(u"""
		given test func 2
		""")
	assert True

@Given("test func 2")
def text(context):
	assert True

@Then("I call by iner")
def inner(context):
	print("I am inner method rock on now")
	assert True

@Then('Text passing')
def step_impl(context):
	assert context.text == "My name is vipin"

@Then("Call by python")
def call_fu(context):
	context.execute_steps(u'''
		Then I call by iner
	''')
	assert True

@Given("Table")
def print_table(context):
	print(str(context.table[0]['name']).encode("UTF-8"))
	assert str(context.table[0]['name']).encode("UTF-8") == "vipin"
