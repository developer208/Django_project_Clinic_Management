const div = document.querySelector("#infinite-table");

const table = document
  .querySelector("#infinite-table")
  .getElementsByTagName("tbody")[0];

const firstName = [
  "Joanna",
  "Ruth",
  "Jared",
  "Nicky",
  "Danilo",
  "Reg",
  "Jill",
  "Eve",
  "Adam"
];

const lastName = [
  "Staub",
  "Snuggs",
  "Hagins",
  "Burditt",
  "Sabbagh",
  "Chiu",
  "Smith",
  "Jackson",
  "Johnson"
];

const loadMore = () => {
  for (let i = 0; i < 20; i++) {
    let row = table.insertRow(-1);
    row.insertCell(0).innerHTML =
      firstName[Math.floor(Math.random() * firstName.length)];
    row.insertCell(1).innerHTML =
      lastName[Math.floor(Math.random() * lastName.length)];
    row.insertCell(2).innerHTML = Math.floor(Math.random() * 101);
  }
};

div.addEventListener("scroll", () => {
  if (div.scrollTop + div.clientHeight >= div.scrollHeight) loadMore();
});

loadMore();
