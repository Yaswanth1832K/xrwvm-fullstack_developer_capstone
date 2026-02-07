import React from 'react';
import "../assets/style.css";
import Header from '../Header/Header';

const Contact = () => {
    return (
        <div>
            <Header />
            <div style={{ margin: "5%" }}>
                <div className="card" style={{ width: "100%" }}>
                    <div className="card-body">
                        <h2 className="card-title" style={{ color: "darkblue" }}>Contact Us</h2>
                        <p className="card-text">
                            Have questions or need support? We'd love to hear from you.
                        </p>
                        <div style={{ marginTop: "20px" }}>
                            <h5>Email</h5>
                            <p>support@cardealership.com</p>

                            <h5>Phone</h5>
                            <p>+1 (555) 123-4567</p>

                            <h5>Address</h5>
                            <p>
                                123 Auto Lane,<br />
                                Motor City, MI 48201
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Contact;
