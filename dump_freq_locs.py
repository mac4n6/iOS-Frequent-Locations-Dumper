#!/usr/bin/python
'''
Copyright (c) 2015, Station  X Labs, LLC
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Station X Labs, LLC nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL STATION  X LABS, LLC BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import ccl_bplist
from time import localtime, gmtime, strftime
import binascii
import sys
import hexdump
import argparse
from argparse import RawTextHelpFormatter
import csv
import simplekml

def getMetadata():
    print "METADATA:"
    print "=============================================================================="

    #METADATA HEADER INFORMATION
    print "\tVersion:\t\t\t\t\t" + str(meta_uids["version"])

    try:
        if meta_uids["lastCleanHouse"] == -1.0:
                print "\tlastCleanHouse Timestamp:\t\t\t-1"
        else:
            lastCleanHouse_timestamp = localtime(meta_uids["lastCleanHouse"] + 978307200)
            print "\tlastCleanHouse Timestamp:\t\t\t" + strftime("%m-%d-%Y %H:%M:%S", lastCleanHouse_timestamp)
    except:
        pass

    try:
        if meta_uids["earliestLatestStateModelEl"]["latestStateModelEl"] == -1.0:
                print "\tlatestStateModelEl Timestamp:\t\t\t-1"
        else:
            latestStateModelEl_timestamp = localtime(meta_uids["earliestLatestStateModelEl"]["latestStateModelEl"] + 978307200)
            print "\tlatestStateModelEl Timestamp:\t\t\t" + strftime("%m-%d-%Y %H:%M:%S", latestStateModelEl_timestamp)
    except:
        pass

    try:
        if meta_uids["earliestLatestStateModelEl"]["earliestStateModelEl"] == -1.0:
                print "\tearliestStateModelEl Timestamp:\t\t\t-1"
        else:
            earliestStateModelEl_timestamp = localtime(meta_uids["earliestLatestStateModelEl"]["earliestStateModelEl"] + 978307200)
            print "\tearliestStateModelEl Timestamp:\t\t\t" + strftime("%m-%d-%Y %H:%M:%S", earliestStateModelEl_timestamp)
    except:
        pass

    try:
        if meta_uids["latestIdentification"] == -1.0:
                print "\tlatestIdentification Timestamp:\t\t\t-1"
        else:
            latestIdentification_timestamp = localtime(meta_uids["latestIdentification"] + 978307200)
            print "\tlatestIdentification Timestamp:\t\t\t" + strftime("%m-%d-%Y %H:%M:%S", latestIdentification_timestamp)
    except:
        pass

    try:
        if meta_uids["lastSequentialClusterIdentification"]  == -1.0:
                print "\tlastSequentialClusterIdentification Timestamp:\t-1"
        else:
            lastSequentialClusterIdentification_timestamp = localtime(meta_uids["lastSequentialClusterIdentification"] + 978307200)
            print "\tlastSequentialClusterIdentification Timestamp:\t" + strftime("%m-%d-%Y %H:%M:%S", lastSequentialClusterIdentification_timestamp)
    except:
        pass

    try:
        if meta_uids["timeIntervalofLastSCI"] == -1.0:
                print "\ttimeIntervalofLastSCI Timestamp:\t\t-1"
        else:
            timeIntervalofLastSCI_timestamp = localtime(meta_uids["timeIntervalofLastSCI"] + 978307200)
            print "\ttimeIntervalofLastSCI Timestamp:\t\t" + strftime("%m-%d-%Y %H:%M:%S", timeIntervalofLastSCI_timestamp)
    except:
        pass

    try:
        if meta_uids["latestIdentification"] == -1.0:
                print "\tlatestIdentification Timestamp:\t\t\t-1"
        else:
            latestIdentification_timestamp = localtime(meta_uids["latestIdentification"] + 978307200)
            print "\tlatestIdentification Timestamp:\t\t\t" + strftime("%m-%d-%Y %H:%M:%S", latestIdentification_timestamp)
    except:
        pass

    #ROUTE DATA
    print "\n\tRoute Information [routes]:"
    try:
        routes = meta_uids["routes"]["NS.objects"]
        print "\t\tRoutes:\t\t\t" + str(routes)
    except:
        print "\t\t<<No Route Data Populated>>"

    #LAST CLUSTER
    try:
        print "\n\tLast Cluster Information:"
        try:
            if meta_uids["lastCluster"]["EntryExit_s"]["entry_s"] == -1.0:
                print "\t\tEntry Timestamp:\t-1"
            else:
                lc_entry =  localtime(meta_uids["lastCluster"]["EntryExit_s"]["entry_s"] + 978307200)
                print "\t\tEntry Timestamp:\t" + strftime("%m-%d-%Y %H:%M:%S", lc_entry)
        except:
            pass 

        try:
            if meta_uids["lastCluster"]["EntryExit_s"]["exit_s"] == -1.0:
                print "\t\tExit Timestamp:\t\t-1"
            else:
                lc_exit =  localtime(meta_uids["lastCluster"]["EntryExit_s"]["exit_s"] + 978307200)
                print "\t\tExit Timestamp:\t\t" + strftime("%m-%d-%Y %H:%M:%S", lc_exit)
        except:
            pass

        try:    
            if meta_uids["lastCluster"]["location"]["timestamp_s"] == -1.0:
                print "\t\tTimestamp:\t\t-1"
            else:
                lc_timestamp = localtime(meta_uids["lastCluster"]["location"]["timestamp_s"] + 978307200)
                print "\t\tTimestamp:\t\t" + strftime("%m-%d-%Y %H:%M:%S", lc_timestamp)
        except:
            pass

        try: 
            lc_lat = meta_uids["lastCluster"]["location"]["Latitude_deg"]
            print "\t\tLatitude:\t\t" + str(lc_lat)
        except:
            pass

        try: 
            lc_long = meta_uids["lastCluster"]["location"]["Longitude_deg"]
            print "\t\tLongitude:\t\t" + str(lc_long)
        except:
            pass

        try: 
            lc_confidence = meta_uids["lastCluster"]["location"]["confidence"]
            print "\t\tConfidence:\t\t" + str(lc_confidence)
        except:
            pass

        try: 
            lc_uncertainty = meta_uids["lastCluster"]["location"]["uncertainty_m"]
            print "\t\tUncertainty:\t\t" + str(lc_uncertainty)
        except:
            pass

        if output_type == "c" or output_type == 'e':
            #loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", lc_timestamp), 'Timestamp','Last Cluster', lc_lat, lc_long, 'Null'])
            loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", lc_entry), 'Entry Timestamp','Last Cluster', lc_lat, lc_long, 'Null'])
            loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", lc_exit), 'Exit Timestamp','Last Cluster', lc_lat, lc_long, 'Null'])
        
        if output_type == "k" or output_type == 'e':
            point = frequent_locations_folder.newpoint(name="Last_Cluster")
            point.description = ("Entry Time: " + strftime("%m-%d-%Y %H:%M:%S", lc_entry) + "\nExit Time: " + strftime("%m-%d-%Y %H:%M:%S", lc_exit))
            point.coords = [(lc_long, lc_lat)]
            point.style.iconstyle.color = simplekml.Color.red
            point.timespan.begin = strftime("%Y-%m-%dT%H:%M:%SZ", lc_entry)
            point.timespan.end = strftime("%Y-%m-%dT%H:%M:%SZ", lc_exit)

    except:
        pass

def RTVisitMonitor():
    print "\nRTVisitMonitor Data:"
    print "=============================================================================="

    #Lat/Long
    try:
        entrySampleLon_deg = meta_uids["visitMonitor"]["entrySampleLon_deg"]
        print "\tentrySampleLon_deg:\t\t\t" + str(entrySampleLon_deg)
    except:
        pass

    try:
        entrySampleLat_deg = meta_uids["visitMonitor"]["entrySampleLat_deg"]
        print "\tentrySampleLat_deg:\t\t\t" + str(entrySampleLat_deg)
    except:
        pass

    try:
        sumLon_deg = meta_uids["visitMonitor"]["sumLon_deg"]
        print "\tsumLon_deg:\t\t\t\t" + str(sumLon_deg)
    except:
        pass

    try:
        sumLat_deg = meta_uids["visitMonitor"]["sumLat_deg"]
        print "\tsumLat_deg:\t\t\t\t" + str(sumLat_deg)
    except:
        pass

    try:
        sumLon2_deg = meta_uids["visitMonitor"]["sumLon2_deg"]
        print "\tsumLon2_deg:\t\t\t\t" + str(sumLon2_deg)
    except:
        pass
    try:
        sumLat2_deg = meta_uids["visitMonitor"]["sumLat2_deg"]
        print "\tsumLat2_deg:\t\t\t\t" + str(sumLat2_deg)
    except:
        pass  

    try:
        entryEdgeDetected = int(meta_uids["visitMonitor"]["entryEdgeDetected"])
        print "\tentryEdgeDetected:\t\t\t" + str(entryEdgeDetected)
    except:
        pass

    #Samples
    try:
        if meta_uids["visitMonitor"]["lastProcessedSampleForAdaption_s"] == -1.0:
                print "\tlastProcessedSampleForAdaption_s:\t-1"
        else:
            lastProcessedSampleForAdaption_s = localtime(meta_uids["visitMonitor"]["lastProcessedSampleForAdaption_s"] + 978307200)
            print "\tlastProcessedSampleForAdaption_s:\t" + strftime("%m-%d-%Y %H:%M:%S", lastProcessedSampleForAdaption_s)
    except:
        pass

    try:
        if meta_uids["visitMonitor"]["lastProcessedSample_s"] == -1.0:
                print "\tlastProcessedSample_s:\t\t\t-1"
        else:
            lastProcessedSample_s = localtime(meta_uids["visitMonitor"]["lastProcessedSample_s"] + 978307200)
        print "\tlastProcessedSample_s:\t\t\t" + strftime("%m-%d-%Y %H:%M:%S", lastProcessedSample_s)
    except:
        pass

    #Entry/Exit
    try:
        if meta_uids["visitMonitor"]["potentialEntry_s"] == -1.0:
                print "\tpotentialEntry_s:\t\t\t-1"
        else:
            potentialEntry_s = localtime(meta_uids["visitMonitor"]["potentialEntry_s"] + 978307200)
            print "\tpotentialEntry_s:\t\t\t" + strftime("%m-%d-%Y %H:%M:%S", potentialEntry_s)
    except:
        pass

    try:
        if meta_uids["visitMonitor"]["potentialExit_s"] == -1.0:
                print "\tpotentialExit_s:\t\t\t-1"
        else:
            potentialExit_s = localtime(meta_uids["visitMonitor"]["potentialExit_s"] + 978307200)
            print "\tpotentialExit_s:\t\t\t" + strftime("%m-%d-%Y %H:%M:%S", potentialExit_s)
    except:
        pass


    #Counts
    try:
        dataPointCnt = meta_uids["visitMonitor"]["dataPointCnt"]
        print "\tdataPointCnt:\t\t\t\t" + str(dataPointCnt)
    except:
        pass

    try:
        outlierCnt = meta_uids["visitMonitor"]["outlierCnt"]
        print "\toutlierCnt:\t\t\t\t" + str(outlierCnt)
    except:
        pass

    try:
        adaptionSampleCnt = meta_uids["visitMonitor"]["adaptionSampleCnt"]
        print "\tadaptionSampleCnt:\t\t\t" + str(adaptionSampleCnt)
    except:
        pass

    #LOI
    try:
        insideAnLoiButStatTimeNotMet = int(meta_uids["visitMonitor"]["insideAnLoiButStatTimeNotMet"])
        print "\tinsideAnLoiButStatTimeNotMet:\t\t" + str(insideAnLoiButStatTimeNotMet)
    except:
        pass
    try:
        insideAnLoi = int(meta_uids["visitMonitor"]["insideAnLoi"])
        print "\tinsideAnLoi:\t\t\t\t" + str(insideAnLoi)
    except:
        pass
    try:    
        if entrySampleLat_deg != -1.0 or entrySampleLon_deg != -1.0: 
            if output_type == "c" or output_type == 'e':
                loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", lastProcessedSampleForAdaption_s), 'lastProcessedSampleForAdaption_s Timestamp','RTVisitMonitor', entrySampleLat_deg, entrySampleLon_deg, 'Null'])
                loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", lastProcessedSample_s), 'lastProcessedSample_s Timestamp','RTVisitMonitor', entrySampleLat_deg, entrySampleLon_deg, 'Null'])
                loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", potentialEntry_s), 'potentialEntry_s Timestamp','RTVisitMonitor', entrySampleLat_deg, entrySampleLon_deg, 'Null'])
                loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", potentialExit_s), 'potentialExit_s Timestamp','RTVisitMonitor', entrySampleLat_deg, entrySampleLon_deg, 'Null'])
    except:
        pass

    #LastVisit
    print "\n\tLast Visit Information [lastVisit]:"
    try:
        lv = meta_uids["visitMonitor"]["lastVisit"]
        try:
            if meta_uids["visitMonitor"]["lastVisit"]["EntryExit_s"]["entry_s"] == -1.0:
                print "\t\tEntry Timestamp:\t-1"
            else:
                lv_entry =  localtime(meta_uids["visitMonitor"]["lastVisit"]["EntryExit_s"]["entry_s"] + 978307200)
                print "\t\tEntry Timestamp:\t" + strftime("%m-%d-%Y %H:%M:%S", lv_entry)
        except:
            pass 

        try:
            if meta_uids["visitMonitor"]["lastVisit"]["EntryExit_s"]["exit_s"] == -1.0:
                print "\t\tExit Timestamp:\t\t-1"
            else:
                lv_exit =  localtime(meta_uids["visitMonitor"]["lastVisit"]["EntryExit_s"]["exit_s"] + 978307200)
                print "\t\tExit Timestamp:\t\t" + strftime("%m-%d-%Y %H:%M:%S", lv_exit)
        except:
            pass

        try:  
            if meta_uids["visitMonitor"]["lastVisit"]["location"]["timestamp_s"] == -1.0:
                print "\t\tTimestamp:\t\t-1"
            else:
                lv_timestamp = localtime(meta_uids["visitMonitor"]["lastVisit"]["location"]["timestamp_s"] + 978307200)
                print "\t\tTimestamp:\t\t" + strftime("%m-%d-%Y %H:%M:%S", lv_timestamp)
        except:
            pass

        try: 
            lv_lat = meta_uids["visitMonitor"]["lastVisit"]["location"]["Latitude_deg"]
            print "\t\tLatitude:\t\t" + str(lv_lat)
        except:
            pass

        try: 
            lv_long = meta_uids["visitMonitor"]["lastVisit"]["location"]["Longitude_deg"]
            print "\t\tLongitude:\t\t" + str(lv_long)
        except:
            pass

        try: 
            lv_confidence = meta_uids["visitMonitor"]["lastVisit"]["location"]["confidence"]
            print "\t\tConfidence:\t\t" + str(lv_confidence)
        except:
            pass

        try: 
            lv_uncertainty = meta_uids["visitMonitor"]["lastVisit"]["location"]["uncertainty_m"]
            print "\t\tUncertainty:\t\t" + str(lv_uncertainty)
        except:
            pass

            if output_type == "c" or output_type == 'e':
                #loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", lv_timestamp), 'Timestamp','Last Visit', lv_lat, lv_long, 'Null'])
                loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", lv_entry), 'Entry Timestamp','Last Visit', lv_lat, lv_long, 'Null'])
                loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", lv_exit), 'Exit Timestamp','Last Visit', lv_lat, lv_long, 'Null'])

        if output_type == "k" or output_type == 'e':
            point = frequent_locations_folder.newpoint(name="Last_Visit")
            point.description = ("Entry Time: " + strftime("%m-%d-%Y %H:%M:%S", lv_entry) + "\nExit Time: " + strftime("%m-%d-%Y %H:%M:%S", lv_exit))
            point.coords = [(lv_long, lv_lat)]
            point.style.iconstyle.color = simplekml.Color.red
            point.timespan.begin = strftime("%Y-%m-%dT%H:%M:%SZ", lv_entry)
            point.timespan.end = strftime("%Y-%m-%dT%H:%M:%SZ", lv_exit)

    except:
        print "\t\t<<No Last Visit Data Populated>>"

    #Outliers
    print "\n\tOutlier Information [tempOutliers]:"
    try:
        tempOutliers = meta_uids["visitMonitor"]["tempOutliers"]["NS.objects"]
        print "\t\ttempOutliers:\t\t\t" + str(tempOutliers)
    except:
        print "\t\t<<No Outlier Data Populated>>"

def getLocations():
    print "============================================================================\n"
    print "LOCATION DATA:"
    print "============================================================================\n"

    for index,item in enumerate(objects):
        
        loc_strings = ""
        loc_strings2 = ""
        lastUpdate_timestamp = ""
        numOfDataPts = ""
        loc_timestamp = ""
        in_outs = ""
        transitions = ""
        entry_timestamp = ""
        exit_timestamp = ""
        transitionlist = ""
        start_timestamp = ""
        stop_timestamp = ""

        #Location Metadata
        print "#####################################################################"
        print "Location Entry Number " + str(index + 1) + ":"

        try:
            if item['stateDepiction']['clusterState']['geocodeDate']["NS.time"] == -1.0:
                print "\tEntry Last Update Timestamp:\t-1"
            else:
                lastUpdate_timestamp = localtime(item['stateDepiction']['clusterState']['geocodeDate']["NS.time"] + 978307200)
                print "\tEntry Last Update Timestamp:\t" + strftime("%m-%d-%Y %H:%M:%S", lastUpdate_timestamp)
        except:
            print "\tEntry Last Update Timestamp:\t<<Not Populated>>"

        #Location BLOB    
        print "\nLocation BLOB Contents:"
        try:
            numOfDataPts = item['stateDepiction']['numOfDataPts']
            print "[DataPoints: " + str(numOfDataPts) + "]\n"
        except:
            pass

        try:
            loc_strings = item['stateDepiction']['clusterState']['placeResult']['data']["NS.data"]
            hexOutput(loc_strings)
        except:
            try:
                loc_strings2 = item['stateDepiction']['clusterState']['mapItem']['data']["NS.data"]
                hexOutput(loc_strings2)
            except:
                print "\t<<Location Blob Content Not Populated>>"

        #Location Details
        print "\nLocation Data:"
        try:
            location_lat = str(item['stateDepiction']['clusterState']['location']["Latitude_deg"])
            print "\tLatitude:\t\t" + location_lat
        except:
            print "\tLatitude:\t\t<<Not Populated>>"

        try:
            location_long = str(item['stateDepiction']['clusterState']['location']["Longitude_deg"])
            print "\tLongitude:\t\t" + location_long
        except:
            print "\tLongitude:\t\t<<Not Populated>>"

        try: 
            print "\tConfidence:\t\t" + str(item['stateDepiction']['clusterState']['location']["confidence"])
        except:
            print "\tConfidence:\t\t<<Not Populated>>"

        try:    
            print "\tUncertainty:\t\t" + str(item['stateDepiction']['clusterState']['location']["uncertainty_m"])
        except:
            print "\tUncertainty:\t\t<<Not Populated>>"

        try:
            if item['stateDepiction']['clusterState']['location']["timestamp_s"] == -1.0:
                print "\tUpdate Timestamp:\t-1"
            else:
                loc_timestamp = localtime(item['stateDepiction']['clusterState']['location']["timestamp_s"] + 978307200)
                print "\tUpdate Timestamp:\t" + strftime("%m-%d-%Y %H:%M:%S", loc_timestamp)
        except:
            print "\tUpdate Timestamp:\t<<Not Populated>>"

        #If you really want the Updated Timestamps, uncomment below:
        #if output_type == "c" or output_type == 'e':
            #loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", lastUpdate_timestamp), 'Last Update Timestamp','Location ' + str(index + 1) , location_lat, location_long, 'Null'])
            #loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", loc_timestamp), 'Update Timestamp','Location ' + str(index + 1) , location_lat, location_long, 'Null'])

        #Location Visits
        print "\nVisits (Entry/Exits):"
        try:
            in_outs = item['stateDepiction']['clusterState']['histEntryExit_s']['NS.objects']
            for index2,item2 in enumerate(in_outs):

                print "\n\tVisit Number: " + str(index2 + 1)

                try:
                    if in_outs[index2]["entry_s"] == -1.0:
                        print "\tEntry Timestamp:\t-1"
                    else:
                        entry_timestamp = localtime(in_outs[index2]["entry_s"] + 978307200)
                        print "\tEntry Timestamp:\t" + strftime("%m-%d-%Y %H:%M:%S", entry_timestamp)
                except:
                    print "\tEntry Timestamp:\t<<Not Populated>>" 

                try:
                    if in_outs[index2]["exit_s"] == -1.0:
                        print "\tExit Timestamp:\t\t-1"
                    else:
                        exit_timestamp = localtime(in_outs[index2]["exit_s"] + 978307200)
                        print "\tExit Timestamp:\t\t" + strftime("%m-%d-%Y %H:%M:%S", exit_timestamp)
                except:
                    print "\tExit Timestamp:\t\t<<Not Populated>>"

                if output_type == "c" or output_type == 'e':
                    loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", entry_timestamp), 'Entry Timestamp','Location ' + str(index + 1) , location_lat, location_long, 'Visit ' + str(index2 + 1)])
                    loccsv.writerow([strftime("%m-%d-%Y %H:%M:%S", exit_timestamp), 'Exit Timestamp','Location ' + str(index + 1) , location_lat, location_long, 'Visit ' + str(index2 + 1)])

                if output_type == "k" or output_type == 'e':
                    point = frequent_locations_folder.newpoint(name="Loc " +str(index + 1) +  " - Visit " + str(index2 + 1))
                    point.description = ("\nEntry Time: " + strftime("%m-%d-%Y %H:%M:%S", entry_timestamp) + "\nExit Time: " + strftime("%m-%d-%Y %H:%M:%S", exit_timestamp))
                    point.coords = [(location_long, location_lat)]
                    point.style.iconstyle.color = simplekml.Color.red
                    point.timespan.begin = strftime("%Y-%m-%dT%H:%M:%SZ", entry_timestamp)
                    point.timespan.end = strftime("%Y-%m-%dT%H:%M:%SZ", exit_timestamp)

        except:
            print "\t<<Visits Data Not Populated>>"

        #Location Transitions - Starts/Stops
        print "\nTransition Data:"
        try:
            transitions = item['stateTransitions']['NS.objects']
            if transitions:
                pass
            else:
                print "\t<<Transition Data Not Populated>>"

            for index3,item3 in enumerate(transitions):
                print "\n\tTransition Number: " + str(index3 + 1)

                try:
                    transitionlist = transitions[index3]["listTransitions"]['NS.objects']
                    #print transitionlist
                    for index4,item4 in enumerate(transitionlist):
                        print "\n\t\tStart/Stop: " + str(index4 + 1)

                        try:
                            print "\t\t\tMotion Activity Type: " + str(item4['motionActivityType'])
                        except:
                            print "\t\t\tMotion Activity Type: <<Not Populated>>"
                         
                        try:   
                            print "\t\t\tRoute UUID: " + str(item4['routeUUID'])
                        except:
                            print "\t\t\tRoute UUID: <<Not Populated>>"

                        try:
                            if item4['start_s'] == -1.0:
                                print "\t\t\tStart Timestamp:\t-1"
                            else:
                                start_timestamp = localtime(item4['start_s'] + 978307200)
                                print "\t\t\tStart Timestamp:\t" + strftime("%m-%d-%Y %H:%M:%S", start_timestamp)
                        except:
                            print "\t\t\tStart Timestamp:\t<<Not Populated>>"

                        try:
                            if item4['stop_s'] == -1.0:
                                print "\t\t\tStop Timestamp:\t\t-1"
                            else:
                                stop_timestamp = localtime(item4['stop_s'] + 978307200)
                                print "\t\t\tStop Timestamp:\t\t" + strftime("%m-%d-%Y %H:%M:%S", stop_timestamp)
                        except:
                            print "\t\t\tStop Timestamp:\t\t<<Not Populated>>"

                except:
                    print "\n\t\tStart/Stop: <<Not Populated>>"

        except:
            print "\nTransition Data: <<Not Populated>>"

        print "\n"

def hexOutput(hex_location_blob):
    print "Hexdump Output:"
    print "----------------------------------------------------------------------------"
    print hexdump.hexdump(hex_location_blob)
    print "----------------------------------------------------------------------------"
    print "Hex Output: "
    print "[" + binascii.hexlify(hex_location_blob) + "]"
    print "----------------------------------------------------------------------------"


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='\
    Parse the iOS "Frequent Locations" StateModel#.archive files. \
    \n\tiOS File Location: /private/var/mobile/Library/Caches/com.apple.routined/\
    \n\tVersion: 1.1\
    \n\tUpdated: 01/24/2015\
    \n\tAuthor: Sarah Edwards | @iamevltwin | mac4n6.com | oompa@csh.rit.edu\
    \n\
    \n\tDependencies:\
    \n\t\thexdump.py: https://pypi.python.org/pypi/hexdump\
    \n\t\tccl_bplist.py: https://github.com/jorik041/ccl-bplist'
        , prog='dump_freq_locs.py'
        , formatter_class=RawTextHelpFormatter)
    parser.add_argument('-output', choices=['k','c','e'], action="store", help="k=KML, c=CSV, e=EVERTHING")
    parser.add_argument('State_Model_Plist_File')
    args = parser.parse_args()

    global output_type
    output_type = None

    statemodelfile = args.State_Model_Plist_File

    plistfile = open(statemodelfile, "rb")
    plist = ccl_bplist.load(plistfile)
    plist_objects = ccl_bplist.deserialise_NsKeyedArchiver(plist, parse_whole_structure=True)
    objects = plist_objects["root"]["stateModelLut"]['NS.objects']
    metadata_objects = plist["$top"]
    meta_uids = plist_objects["root"]

    if args.output == 'c' or args.output == 'e':
        output_type = 'c'
        with open('dump_freq_locs_output.csv', 'wb') as csvfile:
            loccsv = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            loccsv.writerow(['Timestamp', 'Timestamp Type','Data Type', 'Latitude', 'Longitude', 'Other Data'])

            getMetadata()
            RTVisitMonitor()
            getLocations()

    if args.output == 'k' or args.output =='e':
        output_type = 'k'
        kml = simplekml.Kml()
        global frequent_locations_folder
        frequent_locations_folder = kml.newfolder(name="Frequent Locations")

        getMetadata()
        RTVisitMonitor()
        getLocations()

        kml.save("dump_freq_locs_output.kml")

