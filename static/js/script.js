const container = document.querySelector('.container');
const count = document.getElementById('count');
const total = document.getElementById('total');
const clubSelect = document.getElementById('club');

let ticketPrice = +clubSelect.value;

const seatData = {
  vip: 20,        // 20 мест для VIP
  standard: 30,   // 30 мест для Standard
  premium: 15,    // 15 мест для Premium
};

function createSeats(sectionId, seatCount) {
  const section = document.getElementById(sectionId);
  for (let i = 0; i < seatCount; i++) {
    const seat = document.createElement('div');
    seat.classList.add('seat');
    section.appendChild(seat);
  }
}

createSeats('vip-seats', seatData.vip);
createSeats('standard-seats', seatData.standard);
createSeats('premium-seats', seatData.premium);

function updateSelectedCount() {
  const selectedSeats = document.querySelectorAll('.container .seat.selected');

  const selectedSeatsCount = selectedSeats.length;
  count.innerText = selectedSeatsCount;
  total.innerText = selectedSeatsCount * ticketPrice;
}

container.addEventListener('click', (e) => {
  if (e.target.classList.contains('seat') && !e.target.classList.contains('occupied')) {
    e.target.classList.toggle('selected');
    updateSelectedCount();
  }
});

clubSelect.addEventListener('change', (e) => {
  ticketPrice = +e.target.value;
  updateSelectedCount();
});

updateSelectedCount();





