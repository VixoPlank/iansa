function dropdownFabricacion() {
  document.querySelector("#submenuFabricacion").classList.toggle("hidden");
  document.querySelector("#arrowFabricacion").classList.toggle("rotate-0");
}
dropdownFabricacion();

function dropdownMaterias() {
  document.querySelector("#submenuMateriasPrimas").classList.toggle("hidden");
  document.querySelector("#arrowMateriasPrimas").classList.toggle("rotate-0");
}
dropdownMaterias();

// Las 3 lineas cuando aparece la version mobile
function openSidebar() {
  document.querySelector(".sidebar").classList.toggle("hidden");
}
