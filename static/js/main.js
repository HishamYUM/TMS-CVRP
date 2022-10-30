var map, directionsManager;
    function GetMap()
    {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Ajm_tY6mR2Pru3-rf4qr1aeQx0_h6Ttah_EaS1quWJyCwXCvdpKHCtxYOQH9ddqj'
        });

        //Load the directions module.
        Microsoft.Maps.loadModule('Microsoft.Maps.Directions', function () {
            //Create an instance of the directions manager.
            directionsManager = new Microsoft.Maps.Directions.DirectionsManager(map);

            //Create waypoints to route between.
            directionsManager.setRequestOptions({ routeMode: Microsoft.Maps.Directions.RouteMode.driving });

            var ListofCities = ordered_cities

            var waypts = ListofCities.map(city => new Microsoft.Maps.Directions.Waypoint({ address: city }))
            // console.log(waypts);
            waypts.map(waypt => directionsManager.addWaypoint(waypt));

            //Set the request options that avoid highways and uses kilometers.
            directionsManager.setRequestOptions({
                distanceUnit: Microsoft.Maps.Directions.DistanceUnit.km,
                routeAvoidance: [Microsoft.Maps.Directions.RouteAvoidance.avoidLimitedAccessHighway]
            });

            //Make the route line thick and green. Replace the title of waypoints with an empty string to hide the default text that appears.
            directionsManager.setRenderOptions({
                drivingPolylineOptions: {
                    strokeColor: 'yellow',
                    strokeThickness: 4
                },
                waypointPushpinOptions: {
                    title: ''
                }
            });

            //Calculate directions.
            directionsManager.calculateDirections();
        });
    }
    
    // }