#This Python script serves as the main script for the server side program
import subprocess

subprocess.run(["lpr", "Desktop/WirelessPrinter/Server/test.txt"])

x = input("type to exit")