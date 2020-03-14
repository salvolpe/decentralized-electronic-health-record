import React from 'react';
import mapboxgl from 'mapbox-gl';
import "./App.css"

const DEMO_API_KEY = 'pk.eyJ1IjoiYWh5bHRvbjE5IiwiYSI6ImNrN3FrYnFxOTAwOGUzc21jYWFtNzh4aG4ifQ.mXUbDQrYWm7TnEexZJ4f1Q';

mapboxgl.accessToken = DEMO_API_KEY;

class App extends React.Component {
  constructor(props) {
      super(props);
      this.state = {
      lng: 5,
      lat: 34,
      zoom: 2
    };
  }
 componentDidMount() {
   // eslint-disable-next-line
    const map = new mapboxgl.Map({ 
    container: this.mapContainer,
    style: 'mapbox://styles/mapbox/light-v10',
    center: [this.state.lng, this.state.lat],
    zoom: this.state.zoom
  });
}

render() {
  return (
    <div>
      <div className="mapContainer" ref={el => this.mapContainer = el} />
    </div>
    )
  }
}

export default App;
