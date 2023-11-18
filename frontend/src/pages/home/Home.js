import { useNavigate } from "react-router-dom"


const Home = () => {
    
    const navigate = useNavigate();
    const onNavigateToLogin = () => navigate(`/login`)
    const onNavigatetoRegister = () => navigate(`/register`)

    return (
        <div className="home-container">
            <div className="header-body">
                <div className="header-container">
                    <h1>Smart IOT Locker</h1>
                </div>
                
                <div className="header-content">
                    <button type="button" onClick={onNavigateToLogin}>
                        Login
                    </button>
                    <button type="button" onClick={onNavigatetoRegister}>
                        Register
                    </button>
                </div>
            </div>
        </div>
    )
}

export default Home