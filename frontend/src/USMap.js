import React, { useState, useEffect } from 'react';
import { ComposableMap, Geographies, Geography, Marker } from 'react-simple-maps';
import moment from 'moment-timezone';
import { stateData } from './stateData';

const geoUrl = 'https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json';

// State coordinates for marker placement (approximate center)
const stateCoordinates = {
  AL: [-86.9023, 32.8067], AK: [-152.4044, 61.3707], AZ: [-111.4312, 33.7298],
  AR: [-92.3731, 34.9697], CA: [-119.4179, 36.7783], CO: [-105.7821, 39.5501],
  CT: [-72.7554, 41.5978], DE: [-75.5071, 39.3185], FL: [-81.5158, 27.9944],
  GA: [-83.6431, 32.9866], HI: [-157.8583, 21.0943], ID: [-114.7420, 44.2405],
  IL: [-89.3985, 40.3495], IN: [-86.2816, 39.8494], IA: [-93.0977, 42.0115],
  KS: [-96.7265, 38.5266], KY: [-84.6701, 37.6681], LA: [-91.8749, 31.1695],
  ME: [-69.3819, 44.6939], MD: [-76.6412, 39.0639], MA: [-71.5301, 42.2302],
  MI: [-84.5555, 43.3266], MN: [-93.9196, 45.6945], MS: [-89.6787, 32.7416],
  MO: [-92.2896, 38.4561], MT: [-110.4544, 46.9219], NE: [-98.2680, 41.1254],
  NV: [-117.0554, 38.3135], NH: [-71.5639, 43.4525], NJ: [-74.5210, 40.2989],
  NM: [-106.2371, 34.8406], NY: [-74.9481, 42.1657], NC: [-79.8064, 35.6301],
  ND: [-99.7840, 47.5289], OH: [-82.7649, 40.3888], OK: [-96.9289, 35.5653],
  OR: [-122.0709, 44.5720], PA: [-77.1945, 40.5908], RI: [-71.5119, 41.6809],
  SC: [-80.9066, 33.8569], SD: [-99.4388, 44.2998], TN: [-86.6923, 35.7478],
  TX: [-97.5631, 31.0545], UT: [-111.8910, 40.1500], VT: [-72.7107, 44.0459],
  VA: [-78.1690, 37.7693], WA: [-121.4906, 47.3917], WV: [-80.9545, 38.4912],
  WI: [-89.6165, 44.2685], WY: [-107.3025, 42.7559]
};

const USMap = () => {
  const [times, setTimes] = useState({});

  useEffect(() => {
    const updateTimes = () => {
      const newTimes = {};
      stateData.forEach(state => {
        newTimes[state.abbr] = moment().tz(state.timezone).format('h:mm:ss A');
      });
      setTimes(newTimes);
    };

    updateTimes();
    const interval = setInterval(updateTimes, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ width: '100%', maxWidth: '1400px', margin: '0 auto', padding: '20px' }}>
      <div style={{
        backgroundColor: 'white',
        borderRadius: '20px',
        padding: '30px',
        boxShadow: '0 10px 40px rgba(0,0,0,0.2)'
      }}>
        <h1 style={{ textAlign: 'center', color: '#333', marginBottom: '30px', fontSize: '2.5rem' }}>
          US Time Map
        </h1>
        <p style={{ textAlign: 'center', color: '#666', marginBottom: '30px', fontSize: '1.1rem' }}>
          Current Time Across All 50 States
        </p>

      <ComposableMap
        projection="geoAlbersUsa"
        style={{ width: '100%', height: 'auto' }}
      >
        <Geographies geography={geoUrl}>
          {({ geographies }) =>
            geographies.map((geo) => (
              <Geography
                key={geo.rsmKey}
                geography={geo}
                fill="#DDD"
                stroke="#FFF"
                strokeWidth={0.5}
                style={{
                  default: { fill: '#9998DD', outline: 'none' },
                  hover: { fill: '#6665CC', outline: 'none' },
                  pressed: { fill: '#4443AA', outline: 'none' },
                }}
              />
            ))
          }
        </Geographies>

        {stateData.map((state) => {
          const coords = stateCoordinates[state.abbr];
          if (!coords) return null;

          return (
            <Marker key={state.abbr} coordinates={coords}>
              <g>
                <rect
                  x={-22}
                  y={-18}
                  width={44}
                  height={24}
                  fill="white"
                  fillOpacity={0.9}
                  rx={4}
                  stroke="#6665CC"
                  strokeWidth={0.5}
                />
                <text
                  textAnchor="middle"
                  y={-8}
                  style={{
                    fontSize: '9px',
                    fill: '#333',
                    fontWeight: 'bold',
                    pointerEvents: 'none'
                  }}
                >
                  {state.abbr}
                </text>
                <text
                  textAnchor="middle"
                  y={2}
                  style={{
                    fontSize: '7px',
                    fill: '#6665CC',
                    fontWeight: 'bold',
                    fontFamily: 'monospace',
                    pointerEvents: 'none'
                  }}
                >
                  {times[state.abbr] || '...'}
                </text>
              </g>
            </Marker>
          );
        })}
      </ComposableMap>
      </div>
    </div>
  );
};

export default USMap;
