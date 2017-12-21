//
//  ViewController.swift
//  mlAccelData
//
//  Created by Vineeth Yeevani on 12/1/17.
//  Copyright © 2017 Vineeth Yeevani. All rights reserved.
//

import UIKit
import CoreMotion
import CoreLocation
import Firebase

class ViewController: UIViewController {
    var motionManager: CMMotionManager!
    var locationManager:CLLocationManager!
    
    var timer: Timer!
    var label: UILabel!
    var localAccelData: [[Double]] = [[]]
    var timeOfMeasurement: Date!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        motionManager = CMMotionManager()
        motionManager.startAccelerometerUpdates()
        
        //Setup the ui elements
        setupLabel()
        
        //Setup the location services
        initLocationService()
        
        //Start the timer which will repeat every five seconds to save the data
        timer = Timer.scheduledTimer(timeInterval: 0.5, target: self, selector: #selector(getData), userInfo: false, repeats: true)
    }
    
    //Setup ui elements
    func setupLabel() {
        label = UILabel(frame: CGRect(x:view.frame.width * 0.1, y: view.frame.height * 0.45, width: view.frame.width * 0.8, height: view.frame.height * 0.3))
        label.text = "Timer starting in 0.5 seconds"
        label.numberOfLines = 3
        view.addSubview(label)
    }
    
    //Transfer local acceleration and position to firebase
    func transferData(withBlock: @escaping () -> ()) {
        //Set reference to the firebase database
        var ref = Database.database().reference()
        //Create a new child in the database and set the reference to that new child
        ref = ref.childByAutoId()
        
        //Create a time stamp for the database to enable velocity processing in the postproccessor
        let timeStamp = NSDate().timeIntervalSince1970
        
        //Set array for the new child in the array with the form  "xaccel, yaccel, zaccel, lat, long, alt
        ref.setValuesForKeys(["data" : localAccelData, "time" : timeStamp])
        
        //Start the cleanup of local data
        withBlock()
    }
    
    //Add the current xaccel, yaccel, zaccel, lat, long to the local storage array
    func addToLocal(xAccel: Double, yAccel: Double, zAccel: Double, lat: Double, long: Double, alt: Double) {
        let localInstantAccelData = [xAccel, yAccel, zAccel, lat, long, alt]
        localAccelData.append(localInstantAccelData)
        if localAccelData.count == 120 {
            //Transfer the local array to the firebase database for neural net processing
            transferData {
                //Since data has already been transfered the local array can be erased
                self.localAccelData = [[]]
            }
        }
    }
    
    @objc func getData() {
        let locationLat = locationManager.location?.coordinate.latitude
        let locationLong = locationManager.location?.coordinate.longitude
        let altitude = locationManager.location?.altitude
        print(String(describing: locationLat) + ", " + String(describing: locationLong) + ", " + String(describing: altitude))
        if let accelData = motionManager.accelerometerData {
            let xAccel = accelData.acceleration.x
            let yAccel = accelData.acceleration.y
            let zAccel = accelData.acceleration.z
            
            label.text = ("x: " + String(xAccel) + "\ny: " + String(yAccel) + "\nz: " + String(zAccel))
            
            //Add to local array for database export
            addToLocal(xAccel: xAccel, yAccel: yAccel, zAccel: zAccel, lat: locationLat!, long: locationLong!, alt: altitude!)
        }
    }
    
    func initLocationService() {
        locationManager = CLLocationManager()
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
        locationManager.requestAlwaysAuthorization()
        if CLLocationManager.locationServicesEnabled() {
            print("Started location services")
            locationManager.startUpdatingLocation()
        }
    }
}

extension ViewController: CLLocationManagerDelegate {
    
}

