JMETER_VERSION="5.3"
import xml.etree.ElementTree as ET
import argparse
import sys
import fileinput
import pdb

from colorit import *


def countNode(root,element):
    count = 0
    for node in root.iter(element):
        count += 1

    return count

def findThreadGroups(jmx):
    tree = ET.parse(jmx)
    root = tree.getroot()
    element = 'ThreadGroup'
    print(str(countNode(root,element)))

    for node in root.iter(element):
        print(node.attrib)

    return


def validateListeners(jmx):
    tree = ET.parse(jmx)
    root = tree.getroot()
    #Check 10 - Listeners Enable or Disable
    #Find ResultCollector node(s) in the XML
    #for tnode in root.iter('ThreadGroup'):
        #for node in root.iter('ResultCollector'):
            #if str.__contains__(str(node.attrib),'true'):
                #print(node.attrib)

    return 

def findJMeterVersion(jmx):
    tree = ET.parse(jmx)
    # Get JMeter version
    root = tree.getroot()
    jmeterversion = root.items()
    #Check 00 - JMeter Version
    if JMETER_VERSION == jmeterversion[2][1]:
        message=f"JMeter version is {jmeterversion[2][1]}."
        printGreen(message)
    else:
        message=f"Found outdated JMeter version: {jmeterversion[2][1]}."
        printRed(message)
        recommendation = "Consider updating to the latest version of JMeter."
        addRecommendation(recommendation)
    return

def printGreen(message):
    '''
    This function will print if the JMeter test plan passes a check.
    '''
    print(color(f"\u2713 {message}", Colors.green))
    return

def printRed(message):
    '''
    This function will print if the JMeter test plan fails a check.
    '''
    print(color(f"\u2718 {message}", Colors.red))
    return

def addRecommendation(recommendation):
    print(f"Recommendation: {recommendation}\n")    
    return