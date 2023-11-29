import { Link } from "react-router-dom"

const Error = () => {
    
    return (
        <div className="flex flex-col justify-center items-center h-screen w-screen bg-[#EBFEFA]">
            <h1 className="font-bold text-4xl text-center">404 Not Found</h1>
            <p className="mt-4 text-center text-black">
                Navigate to SmartDrop homepage&nbsp;
                <Link to="/" className="text-purple-600 hover:text-purple-700 font-semibold underline">here</Link>
            </p>
        </div>
    )
}
    
export default Error