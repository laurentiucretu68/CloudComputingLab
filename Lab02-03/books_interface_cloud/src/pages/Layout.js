import NavbarComp from "../components/Navbar"
import {Outlet} from "react-router-dom";

function Layout(){
    return(
        <>
            <NavbarComp />
            <Outlet />
        </>
    )
}

export default Layout;