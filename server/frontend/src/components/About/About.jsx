import React from 'react';
import "../assets/style.css";
import Header from '../Header/Header';

const About = () => {
    return (
        <div>
            <Header />
            <div style={{ margin: "5%" }}>
                <div className="card" style={{ width: "100%" }}>
                    <div className="card-body">
                        <h2 className="card-title" style={{ color: "darkblue" }}>About Us</h2>
                        <p className="card-text">
                            Welcome to the Car Dealership Review System!
                        </p>
                        <p className="card-text">
                            Our mission is to provide a transparent platform for car buyers to share their experiences and for dealerships to connect with their customers.
                            Whether you are looking for your next dream car or want to leave feedback about a recent purchase, we are here to help.
                        </p>
                        <p>
                            We feature a wide range of dealerships across the country, complete with reviews and ratings to help you make informed decisions.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default About;
