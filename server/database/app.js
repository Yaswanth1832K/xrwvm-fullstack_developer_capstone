const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const cors = require('cors');

const app = express();
const port = 3030;

app.use(cors());
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

// Load JSON data
const reviews_data = JSON.parse(fs.readFileSync("reviews.json", "utf8"));
const dealerships_data = JSON.parse(fs.readFileSync("dealerships.json", "utf8"));

// MongoDB connection
mongoose.connect("mongodb://mongo_db:27017/dealershipsDB");

// Import models (adjust path if models/ folder exists)
const Reviews = require("./review");
const Dealership = require("./dealership");

// Populate database (NO res usage here)
async function populateDB() {
  try {
    await Reviews.deleteMany({});
    await Reviews.insertMany(reviews_data.reviews);

    await Dealership.deleteMany({});
    await Dealership.insertMany(dealerships_data.dealerships);

    console.log("Database populated successfully");
  } catch (err) {
    console.error("Database population error:", err.message);
  }
}

populateDB();

// Home route
app.get("/", (req, res) => {
  res.send("Welcome to the Mongoose API");
});

// Fetch all reviews
app.get("/fetchReviews", async (req, res) => {
  try {
    const documents = await Reviews.find({});
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Fetch reviews by dealer ID
app.get("/fetchReviews/dealer/:id", async (req, res) => {
  try {
    const documents = await Reviews.find({ dealership: req.params.id });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Fetch all dealerships
app.get("/fetchDealers", async (req, res) => {
  try {
    const dealers = await Dealership.find({});
    res.json(dealers);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Fetch dealerships by state
app.get("/fetchDealers/:state", async (req, res) => {
  try {
    const state = req.params.state.toUpperCase();
    const dealers = await Dealership.find({ state: state });
    res.json(dealers);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Fetch dealer by ID
app.get("/fetchDealer/:id", async (req, res) => {
  try {
    const dealer = await Dealership.findOne({ id: req.params.id });
    res.json(dealer);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Insert review
app.post("/insert_review", async (req, res) => {
  try {
    const documents = await Reviews.find().sort({ id: -1 });
    const new_id = documents.length > 0 ? documents[0].id + 1 : 1;

    const review = new Reviews({
      id: new_id,
      name: req.body.name,
      dealership: req.body.dealership,
      review: req.body.review,
      purchase: req.body.purchase,
      purchase_date: req.body.purchase_date,
      car_make: req.body.car_make,
      car_model: req.body.car_model,
      car_year: req.body.car_year,
    });

    const savedReview = await review.save();
    res.json(savedReview);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
