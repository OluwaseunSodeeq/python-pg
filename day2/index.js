
// EXAMPLES ON VARIABLES, NAMING CONVENTIONS, AND SCOPES
const lastName = "Sodeeq";
let favouriteArtists = ["AG Baby", "Dean Lewis", "Pasuma"];
const favouriteNumber = 21;

// Global scope
const user_best_friend = "Malik Muhamed";

// Function scope
function myFunction() {
    const CONSTANTVALUE = 173;
    console.log(`${CONSTANTVALUE} can only be accessed within this function scope.`);
    console.log(`${lastName} and ${favouriteNumber} can be accessed anywhere.`);
}

// Block scope
if (favouriteNumber > favouriteArtists.length) {
    let favouriteFood = "Amala";
    console.log(`${favouriteFood} is a variable with block scope.`);
    console.log(`${lastName} and ${favouriteArtists} can be accessed anywhere.`);
}
