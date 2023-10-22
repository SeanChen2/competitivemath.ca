import Announcement from "./Announcement"

export default function ContentPanel({title, children}) {
    return (
        <div className="h-full flex flex-col bg-blue-100 border-[2px] border-solid border-blue-800 rounded-2xl overflow-x-hidden drop-shadow-2xl">
            <div className="bg-blue-800 w-full px-6 py-2">
                <h1 className="text-white text-lg">{title}</h1>
            </div>
            <div className="grid place-items-center overflow-auto pt-4">
                {children}
            </div>
        </div>
    )
}
