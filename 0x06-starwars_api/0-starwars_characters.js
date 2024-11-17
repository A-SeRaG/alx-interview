#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Define the API URL
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to fetch the movie data
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  // Parse the response body
  const data = JSON.parse(body);

  // Ensure the movie exists
  if (!data.title) {
    console.error('Movie not found');
    return;
  }

  // Get the list of character URLs
  const characters = data.characters;

  // Fetch and print each character name
  characters.forEach((characterUrl) => {
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
