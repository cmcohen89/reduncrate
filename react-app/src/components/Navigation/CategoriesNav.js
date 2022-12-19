import { NavLink } from "react-router-dom";

const CategoriesNav = () => {
  return (
    <nav className="nav">
      <div className="nav-bar-categories-border" />
      <div className="nav-bar-categories">
        <NavLink to="/category/gear">GEAR</NavLink>
        <NavLink to="/category/style">STYLE</NavLink>
        <NavLink to="/category/cars">CARS</NavLink>
        <NavLink to="/category/tech">TECH</NavLink>
        <NavLink to="/category/shelter">SHELTER</NavLink>
        <NavLink to="/category/vices">VICES</NavLink>
        <NavLink to="/category/body">BODY</NavLink>
        <NavLink to="/category/etc">ETC</NavLink>
      </div>
      <div className="nav-bar-categories-border" />
    </nav>
  )
}

export default CategoriesNav;
